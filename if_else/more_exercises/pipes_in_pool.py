volume_pool_liters = int(input())
pipe_one = int(input())
pipe_two = int(input())
hours_worker_out = float(input())
pool = 0
liter_water_more = 0


if volume_pool_liters >= 1000:
    pipe_one = pipe_one * hours_worker_out
    pipe_two = pipe_two * hours_worker_out
    pool = pool + pipe_one + pipe_two
    print(f"The pool is {pool * 100 / volume_pool_liters:.2f}% full."
          f" Pipe 1: {pipe_one * 100 / pool:.2f}%."
          f" Pipe 2: {pipe_two * 100 / pool:.2f}%.")
else:
    pipe_one = pipe_one * hours_worker_out
    pipe_two = pipe_two * hours_worker_out
    liter_water_more = pool + pipe_one + pipe_two - volume_pool_liters
    print(f"For {hours_worker_out:.2f} hours the pool"
          f" overflows with {liter_water_more:.2f} liters.")

