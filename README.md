# Tiki-Data-Analysis-V2
Pipeline for getting the tiki data to analysis some attributes and making some dashboards

<img src="https://i.ibb.co/bR5YXxp/kafka-kibana.png" style="width: 120%;" />

## Contents

- [Quick Start](#quick-start)
- [Tech](#tech)
- [Reference](#reference)

## <a name="quick-start"></a>Quick Start

### Cluster overview

| Application           | URL                                        |
| --------------------  | ------------------------------------------ |
| Hadoop                | [localhost:9870](http://localhost:9870/)   |
| MapReduce             | [localhost:8089](http://localhost:8089/)   |
| Elasticsearch Cluster | [localhost:27017](http://localhost:27017/) |
| Kafka Cluster         | [localhost:9000](http://localhost:9000/)   |
| JupyterLab            | [localhost:8888](http://localhost:8888/)   |
| Spark Master          | [localhost:8080](http://localhost:8080/)   |

### Prerequisites

- Install [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/)

### Build from Docker Hub

1. Download the source code or clone the repository
2. Build the cluster

```bash
./init.sh
docker-compose up -d
```

3. Remove the cluster by typing

```bash
docker-compose down
```
## <a name="tech"></a>Tech

The project was deployed with only my laptop but simulate the cluster with Docker

### Hadoop

<img src="https://images.prismic.io/clubhouse/81445563b0f9a0f7f1c09860c1bc8fc7980fa5d1_hadoop-data-nodes.png" style="width: 50%;" />


### Apache Spark Standalone Cluster

<img src="https://i.ibb.co/Pz4KsWZ/cluster-architecture.png" style="width: 100%;" />

### Elasticsearch Cluster

<img src="https://i.stack.imgur.com/ET92X.jpg" style="width: 100%;" />

### Kafka Cluster

<img src="https://i.morioh.com/201020/9eae9a14.webp" style="width: 100%;" />

## <a name="reference"></a>References

- [André Perez](https://github.com/cluster-apps-on-docker/spark-standalone-cluster-on-docker)
- [Big Data Europe - Hadoop Docker](https://github.com/big-data-europe/docker-hadoop)
- [Big Data Europe - Spark Docker](https://github.com/big-data-europe/docker-spark)
- [Elasticsearch Cluster with Docker](https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html)
- [Setup Kafka Cluster with Docker](https://www.baeldung.com/ops/kafka-docker-setup)