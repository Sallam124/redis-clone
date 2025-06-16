# 🔧 Redis Clone – Lightweight In-Memory Key-Value Store

## Overview

This project is a simplified clone of [Redis](https://redis.io/) – a high-performance, in-memory key-value store. It is built from scratch to understand core system concepts such as networking, memory management, persistence, and protocol design.

The goal is to create a minimal yet extensible Redis-like server that can handle basic commands (`SET`, `GET`, etc.), support persistence, and mimic Redis' simple communication protocol.

## ✨ Features

- ⚡ Fast in-memory key-value storage
- 🧠 Supports basic commands: `SET`, `GET`, `DEL`
- 🔌 TCP server with custom protocol
- 📝 Append-Only File (AOF) persistence
- 🧪 CLI access using `telnet` or a custom REPL
- 🛠️ Designed to be simple, hackable, and extendable

## 🛠 Tech Stack

- **Language**: Python (can be adapted to C++ or Rust)
- **Socket Programming**: For handling client-server communication
- **Custom Protocol**: Inspired by Redis RESP (REdis Serialization Protocol)
- **File I/O**: For persistent data storage

## 📦 Project Structure

```bash
redis-clone/
│
├── server.py           # Main server logic (TCP, command handling)
├── datastore.py        # In-memory data storage and logic
├── persistence.py      # Logging and loading data from disk
├── protocol.py         # (Optional) Custom protocol parser
├── client.py           # CLI client (optional)
├── README.md           # Project documentation
└── tests/              # Unit tests
