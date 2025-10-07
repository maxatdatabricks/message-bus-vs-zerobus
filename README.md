# Message Bus vs ZeroBus: Streaming Ingestion Performance Comparison

A Databricks demo application that compares the performance and implementation approaches for streaming data ingestion using traditional message bus connectors versus the new ZeroBus API.

## Overview

This project demonstrates two different methods for writing streaming data to Databricks streaming tables:

1. **Traditional Approach**: Using the Lakeflow Connect Kafka connector with Azure Event Hub
2. **Modern Approach**: Using the new ZeroBus API directly

## What's Being Compared

### Lakeflow Connect with Azure Event Hub
- Uses the Databricks Lakeflow Connect Kafka connector
- Connects to an Azure Event Hub topic as the message source
- Data flows through the Kafka-compatible Event Hub interface
- Leverages existing Kafka ecosystem tooling

### ZeroBus API
- Direct integration with Databricks' new ZeroBus streaming API
- Native streaming ingestion without external message bus dependencies
- Simplified architecture with fewer moving parts

## Goals

This demo will help evaluate:
- **Performance**: Throughput and latency differences between the two approaches
- **Complexity**: Implementation and operational overhead
- **Cost**: Infrastructure and operational costs
- **Ease of Use**: Developer experience and maintainability

## Architecture

Both approaches will ingest the same dataset and write to Databricks streaming tables, allowing for direct performance comparison under identical conditions.
