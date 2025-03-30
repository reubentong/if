# Infinity Fiction Task

Here's my dog winning a sausage catching competition,
his breed was 404 however.

![Imgur Image](https://imgur.com/a/7jhUSpS)

## Setup & Run

Project can be run in 2 ways:

### Docker
- Firstly ensure you have 
[Docker](https://docs.docker.com/get-started/get-docker/) installed. 

- Build the image and start the containers with:
```console
   docker compose up --build
```
- Application should be running and accessible at `http://0.0.0.0:8000`,
to view docs use you can also use base path.

- To stop the app you can use
```console
   docker compose down
```

### FastAPI / Uvicorn
- Ensure you have python, e.g. 3.12.0
- Create virtual env
- pip install requirements.txt
- run either:

```console
   fastapi run --reload 
```

```console
   uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

## How to use the api

Api is mostly a copy of the dog api itself. It includes pagination
which mostly matches the original api and can be used like so:

```console
   localhost:8000/breeds?page=1
```

```json
{
  "data": [
    {
      "id": "036feed0-da8a-42c9-ab9a-57449b530b13",
      "type": "breed",
      "attributes": {
        "name": "Affenpinscher",
        "description": "The Affenpinscher is a small and playful breed of dog that was originally bred in Germany for hunting small game. They are intelligent, energetic, and affectionate, and make excellent companion dogs.",
        "life": {
          "max": 16,
          "min": 14
        },
        "male_weight": {
          "max": 5,
          "min": 3
        },
        "female_weight": {
          "max": 5,
          "min": 3
        },
        "hypoallergenic": true
      },
      "relationships": {
        "group": {
          "data": {
            "id": "f56dc4b1-ba1a-4454-8ce2-bd5d41404a0c",
            "type": "group"
          }
        }
      }
    }
.....
```


### Extended functionality
I hate this and have left a [comment](https://github.com/reubentong/if/blob/d45853b1b012edab585b2426fc64c455d4d7bb51/app/services/breed_service.py#L22), but querying without the pagination
will give all results:

```console
   localhost:8000/breeds
```

```json
{
  "data": [
    {
      "id": "036feed0-da8a-42c9-ab9a-57449b530b13",
      "type": "breed",
      "attributes": {
        "name": "Affenpinscher",
        "description": "The Affenpinscher is a small and playful breed of dog that was originally bred in Germany for hunting small game. They are intelligent, energetic, and affectionate, and make excellent companion dogs.",
        "life": {
          "max": 16,
          "min": 14
        },
        "male_weight": {
          "max": 5,
          "min": 3
        },
        "female_weight": {
          "max": 5,
          "min": 3
        },
        "hypoallergenic": true
      },
      "relationships": {
        "group": {
          "data": {
            "id": "f56dc4b1-ba1a-4454-8ce2-bd5d41404a0c",
            "type": "group"
          }
        }
      }
    }
.....
```

Querying with name param will also filter results:

```console
   localhost:8000/breeds?name=Golden
```
or

```console
   localhost:8000/breeds?name=Golden+Retriever
```

```json
{
  "data": [
    {
      "id": "fee91641-2a2e-4c4f-b557-cff67c5803bc",
      "type": "breed",
      "attributes": {
        "name": "Golden Retriever",
        "description": "The Golden Retriever is a large and muscular breed of dog that was originally bred in Scotland for retrieving game. They are intelligent, friendly, and eager to please, and make excellent family pets.",
        "life": {
          "max": 14,
          "min": 12
        },
        "male_weight": {
          "max": 34,
          "min": 29
        },
        "female_weight": {
          "max": 32,
          "min": 25
        },
        "hypoallergenic": false
      },
      "relationships": {
        "group": {
          "data": {
            "id": "ab110192-e41b-43ff-a630-f7aee156b33a",
            "type": "group"
          }
        }
      }
    }
  ],
  "meta": null,
  "links": null
}
```

Look forward to discussing :)

