import logging as log
import asyncio
import time

async def continue_process(process):
  try:
    while not process.stdout.at_eof():
      data = await process.stdout.readline()
      print(data.decode().rstrip())

    code = await process.wait()

    if code < 0:
      log.error(f'Signal received: {-code}')

    return code
  except asyncio.CancelledError as e:
    process.kill()
    raise

async def worker(name, queue):
  while True:
    # Get a "work item" out of the queue.
    item = await queue.get()

    name = item.name()

    print(f'...running {name}')

    try:
      item.builder().prepair(item)
      cwd = item.wd()
      p = await asyncio.create_subprocess_exec("make", "run", cwd = cwd,
                                             stdout = asyncio.subprocess.PIPE,
                                             stderr = asyncio.subprocess.STDOUT)
      code = await continue_process(p)

      if code == 0:
        item.setStatus("+")
        print(f"[PASSED] {name}")
      else:
        print(f"[FAILED] {name} ({code})")
    except Exception as e:
      print(f"[FAILED]: {name} could not start: {e}")

    # Notify the queue that the "work item" has been processed.
    queue.task_done()

async def main(tests, JobCount):
  # Create a queue that we will use to store our "workload".
  queue = asyncio.Queue()

  for test in tests:
    queue.put_nowait(test)

  if JobCount <= 0:
    JobCount = 1

  # Create three worker tasks to process the queue concurrently.
  tasks = []
  log.debug(f"creating {JobCount} worker threads")
  for i in range(JobCount):
    task = asyncio.create_task(worker(f'worker-{i}', queue))
    tasks.append(task)

  # Wait until the queue is fully processed.
  started_at = time.monotonic()
  await queue.join()
  total_elapsed = time.monotonic() - started_at

  print(f"Elapsed: {total_elapsed}")

  # Cancel our worker tasks.
  for task in tasks:
     task.cancel()

  # Wait until all worker tasks are cancelled.
  await asyncio.gather(*tasks, return_exceptions=True)

  print('===')


def runTests(tests, jobCount):
  asyncio.run(main(tests, jobCount))
