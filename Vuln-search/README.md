# 🔍 vuln-search

**vuln-search** is a **self-hosted open-source tool** to search for vulnerabilities and possible exploit mentions related to any equipment or software.  
It searches both:
- 🌍 **Surface web** (latest CVEs from NVD database)
- 🌑 **Dark web** (example .onion sources, using Tor)

Results are displayed in a **local, private web dashboard** you run on your own machine.

> ✅ Made for researchers, pentesters & security enthusiasts.

---

## ✨ Features
- Simple web interface (Flask)
- Enter any equipment or software name (e.g. `Cisco`, `Fortinet`, `Apache`)
- See latest CVEs & mentions
- Self-hosted & private: no cloud, no external servers
- Docker & docker-compose ready
- Dark web search via Tor proxy
- Secure login (username & hashed password)

---

## 📦 Installation

### Requirements
- [Docker](https://www.docker.com/) & [Docker Compose](https://docs.docker.com/compose/)

---

### 🛠 Setup & Run

Clone the repository:

```bash
git clone https://github.com/med--dab/vuln-search.git
cd vuln-search
