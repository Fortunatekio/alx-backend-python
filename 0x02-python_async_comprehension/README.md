asynchronous python
Coroutines are functions which can pause for an input during its execution.
They are similar to python generators but unlike generators which pauses to send result back to caller, coroutines pauses to accept inputs from caller.
you need to define a coroutine function using the async def syntax. This function will be called async_generator and it won't take any arguments.
Within the coroutine function, you'll create a loop that iterates 10 times. You can use range(10) to accomplish this.
Inside the loop, you need to asynchronously wait for 1 second on each iteration. You can use asyncio.sleep(1) to pause the coroutine's execution for 1 second.
After waiting for 1 second, you'll generate a random number between 0 and 10 using the random module.
Finally, you'll yield the generated random number so that it can be consumed by the code that's calling the coroutine.
