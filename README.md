# macchine_coffee_IOT
Ecco la versione del README in **italiano**, organizzata e pronta all’uso:

---

# 🏷 Progetto: Macchina del caffè con CoAP e Python

## ☕ Idea del progetto

Questo progetto mostra come costruire un’applicazione **IoT (Internet of Things)** per controllare una macchina del caffè usando il **protocollo CoAP**.
Obiettivo: trattare la macchina del caffè come **risorse RESTful** e permetterne il controllo e il monitoraggio tramite rete.

---

## 🛠 Risorse (Resources)

### 1️⃣ `/temperature` – Sensore di temperatura

* Mostra la temperatura della macchina.
* JSON di risposta:

```json
{
  "timestamp": "167191910000",
  "value": 32,
  "unit": "C"
}
```

* Operazioni:

  * `GET` → restituisce l’ultima lettura di temperatura
* Codici possibili: `2.05 Content`, `4.00 Bad Request`, `5.00 Internal Server Error`

---

### 2️⃣ `/capsule` – Sensore presenza capsula

* Indica se una capsula è stata inserita nella macchina.
* JSON di risposta:

```json
{
  "timestamp": "167191910000",
  "value": true
}
```

* Operazioni:

  * `GET` → restituisce lo stato della capsula
* Codici possibili: `2.05 Content`, `4.00 Bad Request`, `5.00 Internal Server Error`

---

### 3️⃣ `/coffee` – Attuatore caffè

* Mostra il numero e i tipi di caffè preparati.
* JSON di risposta:

```json
{
 "totalCount": 10,
 "shortCount": 2,
 "mediumCount": 3,
 "longCount": 5
}
```

* Operazioni:

  * `GET` → restituisce lo storico dei caffè
  * `POST` → prepara un caffè corto predefinito
  * `PUT` → invia JSON per selezionare il tipo di caffè (`short`, `medium`, `long`)
* Funzione Observe: i client possono sottoscrivere notifiche per ogni nuovo caffè preparato

---

## ⚙ Configurazione progetto

1. Creare un progetto Python.
2. Installare la libreria CoAP:

```bash
pip install aiocoap
```

---

## 📦 Modelli dati (Model Classes)

| Classe                            | Descrizione                                       |
| --------------------------------- | ------------------------------------------------- |
| `TemperatureSensorDescriptor`     | Rappresenta una lettura casuale della temperatura |
| `CapsulePresenceSensorDescriptor` | Rappresenta lo stato della capsula (true/false)   |
| `CoffeeHistoryDescriptor`         | Tiene traccia del numero di ciascun tipo di caffè |

### Classe richiesta caffè

* Rappresenta il corpo del `PUT`:

```json
{ "type": "medium" }
```

* Valori possibili: `short`, `medium`, `long`

---

## 🖥 Implementazione risorse in Python

* `/temperature` → eredita da `resource.Resource` e restituisce JSON
* `/capsule` → stessa logica, valore casuale
* `/coffee` → eredita `ObservableResource` e implementa:

  * `render_get()` → restituisce lo storico del caffè
  * `render_post()` → prepara un caffè corto
  * `render_put()` → prepara un caffè in base al tipo e poi `self.updated_state()` per notificare i client osservatori

---

## 🌐 Server CoAP

* File: `coffee_machine_coap_process.py`
* Crea l’albero delle risorse:

```
/temperature
/capsule
/coffee
```

* Funziona su: `127.0.0.1:5683` usando `asyncio`

---

## 🧪 Programmi client di test

| Programma        | Funzione                        |
| ---------------- | ------------------------------- |
| GET Client       | Test lettura valori             |
| Observing Client | Sottoscrizione a `/coffee`      |
| POST Client      | Prepara caffè corto             |
| PUT Client       | Prepara caffè di tipo specifico |

---

## ✅ Conclusioni

Questo progetto insegna:

* Come progettare un dispositivo IoT come **risorse REST**
* Come far funzionare un server CoAP in Python
* Lettura e scrittura di dati JSON
* Implementazione di sensori e attuatori
* Uso della funzione **Observe**
* Test del server con più client


