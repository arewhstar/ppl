## 🚀 Features

- Fetches random people from [randomuser.me](https://randomuser.me) API
- Stores them in a PostgreSQL database
- Two separate services running and fetching different nationality people (configurable)
- Logs every API request to a history table

## 🛠️ Requirements

- [Podman](https://podman.io/) installed and available in your system path  
  (You can alternatively use Docker with slight modifications)

## ⚙️ Setup & Usage

     ```bash
   git clone https://github.com/your-username/ppl.git
   cd ppl
   make run-all
   ```

**This will:**

- Start a PostgreSQL container
- Build two separate Python service containers (e.g., for us and hun)
- Run both services in the background

## ⚙️ Endpoints

    ```bash
    http://localhost:8080/person/{firstname}
    http://localhost:8081/person/{firstname}
    ```

## 🛑 Stop
    ```bash
    make stop-all
    ```