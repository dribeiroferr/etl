# API Gateway 🌐

![API Gateway Banner](path_to_your_image.png) 

> A modern API Gateway built with FastAPI, Kong, and SQL Server. 🚀

---

## 🎨 Color Theme

This project follows a dark-themed color palette with shades of purple. 

![Color Palette](path_to_color_palette_image.png)

---

## 📚 Table of Contents

- [API Gateway 🌐](#api-gateway-)
  - [🎨 Color Theme](#-color-theme)
  - [📚 Table of Contents](#-table-of-contents)
  - [🌟 Features](#-features)
  - [🛠 Installation](#-installation)
  - [🎨 Color Theme](#-color-theme-1)
  - [📚 Table of Contents](#-table-of-contents-1)
  - [🌟 Features](#-features-1)
  - [🛠 Installation](#-installation-1)
  - [🚀 Usage](#-usage)
  - [**POST /v1/gateway/save/request\_response**](#post-v1gatewaysaverequest_response)
  - [📂 Project Structure](#-project-structure)
  - [🧪 Testing](#-testing)
  - [🤝 Contributing](#-contributing)
  - [📜 License](#-license)
  - [📞 Contact](#-contact)

---

## 🌟 Features

- **FastAPI Integration**: Harness the power and speed of FastAPI.
- **Kong API Gateway**: Robust management of incoming API requests.
- **SQL Server Backend**: Reliable and scalable database solution.
- **Modern Logging**: Comprehensive logging for requests and responses.
- **Hexagonal Architecture**: Maintainability and scalability at its core.

---

## 🛠 Installation

1. **Clone the repository**:

   ```
   git clone https://github.com/your_username/apigateway.git# API Gateway 🌐
   ```

![API Gateway Banner](path_to_your_image.png) 

> A modern API Gateway built with FastAPI, Kong, and SQL Server. 🚀

---

## 🎨 Color Theme

This project follows a dark-themed color palette with shades of purple. 

![Color Palette](path_to_color_palette_image.png)

---

## 📚 Table of Contents

- [API Gateway 🌐](#api-gateway-)
  - [🎨 Color Theme](#-color-theme)
  - [📚 Table of Contents](#-table-of-contents)
  - [🌟 Features](#-features)
  - [🛠 Installation](#-installation)
  - [🎨 Color Theme](#-color-theme-1)
  - [📚 Table of Contents](#-table-of-contents-1)
  - [🌟 Features](#-features-1)
  - [🛠 Installation](#-installation-1)
  - [🚀 Usage](#-usage)
  - [**POST /v1/gateway/save/request\_response**](#post-v1gatewaysaverequest_response)
  - [📂 Project Structure](#-project-structure)
  - [🧪 Testing](#-testing)
  - [🤝 Contributing](#-contributing)
  - [📜 License](#-license)
  - [📞 Contact](#-contact)

---

## 🌟 Features

- **FastAPI Integration**: Harness the power and speed of FastAPI.
- **Kong API Gateway**: Robust management of incoming API requests.
- **SQL Server Backend**: Reliable and scalable database solution.
- **Modern Logging**: Comprehensive logging for requests and responses.
- **Hexagonal Architecture**: Maintainability and scalability at its core.

---

## 🛠 Installation

1. **Clone the repository**:

   ```
   git clone https://github.com/sigaodavi/apigateway.git
   ```
2. **Navigate to the project directory**:
   ```
   cd apigateway
   ```
3. **Set up the environment**:
   ```
   cp src/.env.example src/.env
   ```
   Modify the '.env' file with your settings
4. **Run with Docker Compoose**:
   ```
   docker-compose up -d
   ``` 
---

## 🚀 Usage

1. **Access the API**:
   Open your browser or API client and navigate to:**"http://localhost:9001"**
2. **API Endpoints**:
   - Save Request:<br>
   **POST /v1/gateway/save/request_response**   
---

## 📂 Project Structure

```
apigateway/
│
├── .git/                           # Git version control folder
├── .pytest_cache/                  # Temporary cache for pytest
├── etc/                            # Configuration and setup files
│   ├── database/                   
│   │   ├── sqlServer/              # SQL Server setup files
│   │   │   └── Dockerfile          
│   │   ├── kong/                   # Kong API Gateway setup files
│   │       └── Dockerfile          
│   └── ...                         # Other configuration files
│
├── src/                            # Source code
│   ├── gateway/
│   │   ├── domain/                 # Domain logic
│   │   │   ├── logging/            # Logging related files
│   │   │   ├── request/            # Request related files
│   │   │   └── response/           # Response related files
│   │   ├── application/            # Application services
│   │   │   └── requestResponse/    # Request-Response service
│   │   ├── infrastructure/         # Infrastructure related files
│   │   │   ├── database/           # Database related files
│   │   │   ├── logging/            # Logging infrastructure
│   │   │   └── middleware/         # Middleware related files
│   │   └── main.py                 # Main application entry point
│   └── ...                         # Other source files
│
├── scripts/                        # Utility scripts
│   ├── register_fastapi.sh
│   ├── add_plugins.sh
│   └── ...
│
├── tests/                          # Test files
│   ├── domain/                     # Domain logic tests
│   ├── application/                # Application services tests
│   ├── infrastructure/             # Infrastructure tests
│   └── ...
│
├── docker-compose.yml              # Docker Compose configuration
└── README.md                       # Project documentation
```

## 🧪 Testing

To run the tests, execute the following command:
```
pytest src/tests
```
## 🤝 Contributing

We welcome contributions from the community! Whether it's bug reports, feature requests, or code contributions, your input is valuable. For guidelines on how to contribute, please refer to the [CONTRIBUTING.md](CONTRIBUTING.md) file.

---

## 📜 License

This project is under the MIT License. For more details, please check the [LICENSE](LICENSE) file.

---

## 📞 Contact

Got questions or feedback? Reach out!

- **Application Owner**: Davi Ferreira (Sr. Fullstack Engineer)
- **GitHub**: [@sigaodavi](https://github.com/sigaodavi)
- **Email**: davi.ferreira.terceirizado@sigaantenado.com.br

---

**Happy Coding!** 💜