# API Gateway with NGINX

1. **Download Docker**

    Follow the instructions to install Docker from [Docker Documentation](https://docs.docker.com/get-docker/).

2. **Download Nginx and start the service**

    Download Nginx

    ```bash
    sudo apt update
    sudo apt install nginx
    sudo systemctl start nginx
    sudo systemctl enable nginx
    ```

3. **Add the host in /etc/hosts**

    Edit the file `/etc/hosts` to add the host `bookstore.io`:

    ```bash
    sudo nano /etc/hosts
    ```

    Then, add the line at the file:

    ```text
    127.0.0.1    localhost bookstore.io
    ```

    Save and close the file (with `CTRL+X`, then `Y` and `Enter`).

4. **Run the script**

    Now, run the script `run.sh` to start the the Docker containers:

    ```bash
    sudo ./run.sh
    ```
5. **Test the endpoints**

    GET books, return the saved books.
    ```bash
    curl -ik --header "apikey:abc123" --request GET  https://bookstore.io/api/bookstore/catalog/books
    ```

    GET books by Id, return the saved books by Id.
    ```bash
    curl -ik --header "apikey:abc123" --request GET  https://bookstore.io/api/bookstore/catalog/books/1
    ```

    GET stores, return the saved stores.
    ```bash
    curl -ik --header "apikey:abc123" --request GET  https://bookstore.io/api/bookstore/stores/stores
    ```
    
    Error 403, Forbidden
    ```bash
    curl -ik --header "apikey:XXXXXXX" --request GET  https://bookstore.io/api/bookstore/stores/stores
    ```
    Error 402, Unathorized
    ```bash
    curl -ik --request GET  https://bookstore.io/api/bookstore/catalog/books
    ```