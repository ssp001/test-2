
'wsl.exe --update'.

-- Probelm 
"""Traceback (most recent call last):
  File "C:\Users\shova\Desktop\project\test-2\.venv\lib\site-packages\uvicorn\protocols\http\h11_impl.py", line 403, in run_asgi
    result = await app(  # type: ignore[func-returns-value]
  File "C:\Users\shova\Desktop\project\test-2\.venv\lib\site-packages\uvicorn\middleware\proxy_headers.py", line 60, in __call__
    return await self.app(scope, receive, send)
  File "C:\Users\shova\Desktop\project\test-2\.venv\lib\site-packages\fastapi\applications.py", line 1134, in __call__
    await super().__call__(scope, receive, send)
  File "C:\Users\shova\Desktop\project\test-2\.venv\lib\site-packages\starlette\applications.py", line 113, in __call__
    await self.middleware_stack(scope, receive, send)
  File "C:\Users\shova\Desktop\project\test-2\.venv\lib\site-packages\starlette\middleware\errors.py", line 186, in __call__
    raise exc
  File "C:\Users\shova\Desktop\project\test-2\.venv\lib\site-packages\starlette\middleware\errors.py", line 164, in __call__
    await self.app(scope, receive, _send)
  File "C:\Users\shova\Desktop\project\test-2\.venv\lib\site-packages\starlette\middleware\exceptions.py", line 63, in __call__
    await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
  File "C:\Users\shova\Desktop\project\test-2\.venv\lib\site-packages\starlette\_exception_handler.py", line 53, in wrapped_app
    raise exc
  File "C:\Users\shova\Desktop\project\test-2\.venv\lib\site-packages\starlette\_exception_handler.py", line 42, in wrapped_app
    await app(scope, receive, sender)
  File "C:\Users\shova\Desktop\project\test-2\.venv\lib\site-packages\fastapi\middleware\asyncexitstack.py", line 18, in __call__
    await self.app(scope, receive, send)
  File "C:\Users\shova\Desktop\project\test-2\.venv\lib\site-packages\starlette\routing.py", line 716, in __call__
    await self.middleware_stack(scope, receive, send)
  File "C:\Users\shova\Desktop\project\test-2\.venv\lib\site-packages\starlette\routing.py", line 736, in app
    await route.handle(scope, receive, send)
  File "C:\Users\shova\Desktop\project\test-2\.venv\lib\site-packages\starlette\routing.py", line 290, in handle
    await self.app(scope, receive, send)
  File "C:\Users\shova\Desktop\project\test-2\.venv\lib\site-packages\fastapi\routing.py", line 124, in app
    await wrap_app_handling_exceptions(app, request)(scope, receive, send)
  File "C:\Users\shova\Desktop\project\test-2\.venv\lib\site-packages\starlette\_exception_handler.py", line 53, in wrapped_app
    raise exc
  File "C:\Users\shova\Desktop\project\test-2\.venv\lib\site-packages\starlette\_exception_handler.py", line 42, in wrapped_app
    await app(scope, receive, sender)
  File "C:\Users\shova\Desktop\project\test-2\.venv\lib\site-packages\fastapi\routing.py", line 110, in app
    response = await f(request)
  File "C:\Users\shova\Desktop\project\test-2\.venv\lib\site-packages\fastapi\routing.py", line 390, in app
    raw_response = await run_endpoint_function(
  File "C:\Users\shova\Desktop\project\test-2\.venv\lib\site-packages\fastapi\routing.py", line 291, in run_endpoint_function
    return await run_in_threadpool(dependant.call, **values)
  File "C:\Users\shova\Desktop\project\test-2\.venv\lib\site-packages\starlette\concurrency.py", line 38, in run_in_threadpool
    return await anyio.to_thread.run_sync(func)
  File "C:\Users\shova\Desktop\project\test-2\.venv\lib\site-packages\anyio\to_thread.py", line 56, in run_sync
    return await get_async_backend().run_sync_in_worker_thread(
  File "C:\Users\shova\Desktop\project\test-2\.venv\lib\site-packages\anyio\_backends\_asyncio.py", line 2485, in run_sync_in_worker_thread
    return await futures
  File "C:\Users\shova\Desktop\project\test-2\.venv\lib\site-packages\anyio\_backends\_asyncio.py", line 976, in run
    result = context.run(func, *args)
  File "C:\Users\shova\Desktop\project\test-2\Backend\backend.py", line 109, in predict_digonasis
    encoded = Oe.fit_transform([[loop]])[0]
  File "C:\Users\shova\Desktop\project\test-2\.venv\lib\site-packages\sklearn\utils\_set_output.py", line 316, in wrapped
    data_to_wrap = f(self, X, *args, **kwargs)
  File "C:\Users\shova\Desktop\project\test-2\.venv\lib\site-packages\sklearn\base.py", line 894, in fit_transform
    return self.fit(X, **fit_params).transform(X)
  File "C:\Users\shova\Desktop\project\test-2\.venv\lib\site-packages\sklearn\base.py", line 1365, in wrapper
    return fit_method(estimator, *args, **kwargs)
  File "C:\Users\shova\Desktop\project\test-2\.venv\lib\site-packages\sklearn\preprocessing\_encoders.py", line 1515, in fit
    fit_results = self._fit(
  File "C:\Users\shova\Desktop\project\test-2\.venv\lib\site-packages\sklearn\preprocessing\_encoders.py", line 83, in _fit
    X_list, n_samples, n_features = self._check_X(
  File "C:\Users\shova\Desktop\project\test-2\.venv\lib\site-packages\sklearn\preprocessing\_encoders.py", line 49, in _check_X
    X_temp = check_array(X, dtype=None, ensure_all_finite=ensure_all_finite)
  File "C:\Users\shova\Desktop\project\test-2\.venv\lib\site-packages\sklearn\utils\validation.py", line 1099, in check_array
    raise ValueError(
ValueError: Found array with dim 4, while dim <= 2 is required.
"""

2025-11-06 16:15:29.112670: I tensorflow/core/util/port.cc:153] oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`.
2025-11-06 16:15:30.959518: I tensorflow/core/util/port.cc:153] oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`.