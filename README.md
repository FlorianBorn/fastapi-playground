# fastapi-playground
Deploy a FastML Model with FastAPI

# Hello_World
Goal: build the first app with FastAPI
Source: https://fastapi.tiangolo.com/tutorial/first-steps/
Examples: https://fastapi.tiangolo.com/#example (How to run, async & wait, How to use uvicorn, API docs)


Steps:
1. Install FastAPI
    ```pip install fastapi[all]```
2. Create a main.py file
    ``` 
        from fastapi import FastAPI

        app = FastAPI()


        @app.get("/")
        def read_root():
            return {"Hello": "World"}


        @app.get("/items/{item_id}")
        def read_item(item_id: int, q: str = None):
            return {"item_id": item_id, "q": q}
    ```
3. Run the application
    ```uvicorn main:app --reload```
4. Check the app
    ```http://localhost:8000/```
5. Check the automatic generated documentation
    ```http://localhost:8000/docs```