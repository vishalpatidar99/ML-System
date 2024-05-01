## Installation

To install the ML-System repository, follow these steps:

1. Clone the git repository:
    ```sh
    git clone https://github.com/vishalpatidar99/ML-System.git
    cd ML-System
    ```

2. Build and start the server using Docker Compose:
    ```sh
    docker-compose up --build
    ```

### Obtaining Access Token

To obtain an access token for authentication, import the following curl request into Postman:

```sh
curl --location 'http://127.0.0.1:8000/oauth/token/' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Authorization: Basic M1EwTTBPTFVRUktMVGdielRUMVpsMFNRdzNkSWhDeTBieXhtemZlVzpZVWhnRFk4dFFWclVkY0pLVW9xakZ3b05ZNlNIRVRiUElYNzVUWGZwbmtDaW9RM1h5enFEUW1TdXlQeVlGQ2R6TWxvU1Y5cEVMbDV6ZkpWUkxtejhzVHpOQmlzNDM2amZkVU1lVDVUdXBvbXNzRHlGWnFpNjNGS2I2OXc5VkFKaQ==' \
--data-urlencode 'grant_type=password' \
--data-urlencode 'username=groot' \
--data-urlencode 'password=root'
```

Now, again import following curl
This is the API to upload .txt file
```sh
curl --location 'http://127.0.0.1:8000/api/upload-img/' \
--header 'Authorization: Bearer Lc1k5BBfaSDY8Hk8EDVlVeIWgvVw0J' \
--form 'files=@"/C:/Users/deepe/Downloads/demo.txt"'
```

**Note: Change token if required**