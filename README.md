# System Design Learning Journey

A structured study plan covering Low-Level Design (LLD), High-Level Design (HLD), distributed systems, databases, and production architecture. This repo tracks my progress, notes, and design exercises across each phase.

## Timeline

~6–9 months at 10–15 hrs/week, then continuous.

## Structure

- `phase-XX-topic/` — notes, diagrams, and exercises for each phase
- `case-studies/` — design exercises (Design Twitter, Design Uber, etc.)
- `patterns/` — design pattern implementations
- `papers/` — distributed systems paper notes

---

## Phase 1 — Foundations

**Topics**

- Networking: TCP/IP, UDP, HTTP/1.1, HTTP/2, HTTP/3, WebSockets, DNS, TLS
- OS basics: processes, threads, concurrency, context switching, file I/O
- Memory: stack vs heap, garbage collection, memory leaks
- Computer architecture: CPU caches, latency numbers every engineer should know
- Linux fundamentals: signals, file descriptors, sockets, /proc

**Resources**

- *Computer Networking: A Top-Down Approach* — Kurose, Ross
- *Operating Systems: Three Easy Pieces* — pages.cs.wisc.edu/~remzi/OSTEP/ (free)
- *High Performance Browser Networking* — Ilya Grigorik (free at hpbn.co) — the definitive networking book for backend engineers
- Hussein Nasser — YouTube (networking deep dives)
- "Latency Numbers Every Programmer Should Know" — Jeff Dean
- Julia Evans — zines and blog posts (jvns.ca)

---

## Phase 2 — Low-Level Design (LLD)

**Topics**

- OOP fundamentals: encapsulation, inheritance, polymorphism, composition
- SOLID principles
- DRY, KISS, YAGNI
- Design patterns:
  - Creational: Singleton, Factory, Abstract Factory, Builder, Prototype
  - Structural: Adapter, Decorator, Facade, Proxy, Composite, Bridge
  - Behavioral: Observer, Strategy, Command, State, Iterator, Template Method, Chain of Responsibility
- UML: class diagrams, sequence diagrams, state diagrams
- Clean code, refactoring, code smells
- Domain modeling
- Test-driven development

**Resources**

- *Head First Design Patterns* — Freeman, Robson (2nd ed., 2020)
- *Design Patterns: Elements of Reusable Object-Oriented Software* — Gang of Four
- *Clean Code* — Robert C. Martin
- *Refactoring* — Martin Fowler (2nd ed., 2018)
- *The Pragmatic Programmer* — Hunt, Thomas (20th Anniversary Edition, 2019)
- Refactoring.guru — design patterns reference

**Projects**

- Design parking lot (classic LLD problem)
- Design elevator system
- Design library management system
- Design Splitwise / expense splitter
- Design rate limiter

---

## Phase 3 — Databases Deep Dive

**Topics**

- Relational model, normalization (1NF–3NF, BCNF), denormalization
- SQL deep dive: joins, window functions, CTEs, query optimization
- Indexes: B-tree, hash, bitmap, covering indexes, when indexes hurt
- Transactions: ACID, isolation levels, MVCC, locking
- Storage engines: row-oriented vs column-oriented, LSM trees vs B-trees
- Replication: leader-follower, multi-leader, leaderless
- Partitioning / sharding strategies
- NoSQL families: document (MongoDB), key-value (Redis, DynamoDB), wide-column (Cassandra), graph (Neo4j)
- Consistency models: strong, eventual, causal, read-your-writes
- CAP theorem, PACELC

**Resources**

- ***Designing Data-Intensive Applications, 2nd Edition*** — Martin Kleppmann & Chris Riccomini (O'Reilly, Feb 2026) — the bible, read cover to cover
- *Database Internals* — Alex Petrov
- Use The Index, Luke! — use-the-index-luke.com
- Asli Engineering by Arpit Bhayani — YouTube (database internals)
- CMU 15-445 Database Systems — Andy Pavlo (free lectures, Spring 2026 current)
- CMU 15-721 Advanced Database Systems

**Projects**

- Build a key-value store from scratch
- Implement a B-tree and an LSM tree
- Write a SQL query optimizer (toy version)

---

## Phase 4 — High-Level Design (HLD) Building Blocks

**Topics**

- Load balancers: L4 vs L7, algorithms (round-robin, least connections, consistent hashing)
- Caching: client-side, CDN, reverse proxy, application, database
  - Strategies: cache-aside, write-through, write-back, write-around
  - Eviction policies: LRU, LFU, FIFO, ARC
- CDNs: how they work, edge locations, cache invalidation
- Message queues & event streaming: Kafka, RabbitMQ, SQS, Pub/Sub
  - Delivery guarantees: at-most-once, at-least-once, exactly-once
- API gateways
- Reverse proxies (Nginx, Envoy)
- Search: inverted indexes, Elasticsearch, OpenSearch
- Rate limiting algorithms: token bucket, leaky bucket, sliding window
- Pagination strategies: offset, cursor, keyset

**Resources**

- *System Design Interview Vol 1 & 2* — Alex Xu
- *Fundamentals of Software Architecture* — Mark Richards, Neal Ford (O'Reilly, 2020)
- *Software Architecture: The Hard Parts* — Mark Richards, Neal Ford (O'Reilly, 2021)
- ByteByteGo — bytebytego.com + YouTube
- The System Design Primer — github.com/donnemartin/system-design-primer
- High Scalability — highscalability.com (less active now, archive is gold)
- Gaurav Sen — YouTube

---

## Phase 5 — Distributed Systems

**Topics**

- Why distributed systems are hard: partial failure, unreliable networks, clocks
- Time, clocks, ordering: physical clocks, logical clocks, vector clocks, hybrid logical clocks
- Consensus: Paxos, Raft, ZAB
- Leader election
- Distributed transactions: 2PC, 3PC, Saga pattern
- Eventual consistency, CRDTs
- Quorum systems, read/write quorums
- Gossip protocols
- Consistent hashing
- Bloom filters, HyperLogLog, Count-Min Sketch
- Distributed tracing
- Idempotency, exactly-once semantics
- Backpressure, circuit breakers, bulkheads

**Resources**

- *Understanding Distributed Systems, 2nd Edition* — Roberto Vitillo (2022) — gentler intro, read first
- *Designing Data-Intensive Applications, 2nd Edition* — Kleppmann & Riccomini (Part II & III)
- MIT 6.5840 (formerly 6.824) Distributed Systems — Robert Morris, Frans Kaashoek (free lectures + Raft labs in Go)
- *Distributed Systems* — Maarten van Steen, Andrew Tanenbaum (free PDF)
- Murat Demirbas blog — muratbuffalo.blogspot.com
- The Morning Paper — blog.acolyer.org (archived since 2021, but archive is invaluable)
- Aphyr's Jepsen analyses — jepsen.io

**Projects**

- Implement Raft consensus
- Build a distributed key-value store with replication
- Implement consistent hashing

---

## Phase 6 — Microservices & API Design

**Topics**

- Monolith vs microservices: tradeoffs, when to split
- Service decomposition: bounded contexts, domain-driven design
- Communication: synchronous (REST, gRPC, GraphQL) vs asynchronous (events)
- API design: REST principles, resource modeling, versioning, pagination, errors
- gRPC: Protocol Buffers, streaming
- GraphQL: schema design, N+1 problem, federation
- Service discovery
- Service mesh: Istio, Linkerd
- API gateway patterns
- BFF (Backend for Frontend)
- Event-driven architecture, event sourcing, CQRS
- Inter-service authentication: mTLS, JWT, OAuth2

**Resources**

- *Building Microservices* — Sam Newman (2nd ed., 2021)
- *Domain-Driven Design* — Eric Evans
- *Implementing Domain-Driven Design* — Vaughn Vernon
- *Microservices Patterns* — Chris Richardson
- microservices.io — Chris Richardson's pattern catalog
- Martin Fowler's blog — martinfowler.com

**Projects**

- Decompose a monolith into services
- Build a service mesh demo with Istio
- Event-sourced order management system

---

## Phase 7 — Reliability, Observability & Security

**Topics**

- SLI / SLO / SLA, error budgets
- The four golden signals: latency, traffic, errors, saturation
- Logging: structured logs, log aggregation (ELK, Loki)
- Metrics: Prometheus, Grafana, time-series databases
- Distributed tracing: OpenTelemetry, Jaeger, Zipkin
- Chaos engineering
- Failure modes, postmortems, blameless culture
- High availability, disaster recovery, RPO/RTO
- Security:
  - Authentication & authorization (OAuth2, OIDC, SAML)
  - Encryption at rest and in transit
  - Secrets management (Vault, KMS)
  - OWASP Top 10
  - Zero trust architecture
  - DDoS mitigation

**Resources**

- *Site Reliability Engineering* — Google (free at sre.google/books)
- *The Site Reliability Workbook* — Google (free at sre.google/books)
- *Release It!* — Michael Nygard (2nd ed., 2018)
- *Database Reliability Engineering* — Campbell, Majors
- *The DevOps Handbook* — Kim, Humble, Debois, Willis
- OWASP — owasp.org
- Brendan Gregg — performance and observability (brendangregg.com)

---

## Phase 8 — Cloud & Infrastructure

**Topics**

- Cloud fundamentals: IaaS, PaaS, SaaS, FaaS
- Compute: VMs, containers, serverless
- Storage: object (S3), block, file, archive
- Networking: VPC, subnets, security groups, NAT, peering
- Containers: Docker internals, image layers, namespaces, cgroups
- Kubernetes: pods, deployments, services, ingress, operators, CRDs
- Infrastructure as Code: Terraform, Pulumi
- CI/CD: pipelines, blue-green, canary, feature flags
- The Twelve-Factor App
- Multi-region, multi-cloud strategies
- Cost optimization

**Resources**

- *Kubernetes in Action* — Marko Lukša
- *Kubernetes Up & Running* — Hightower, Burns, Beda
- *Terraform: Up & Running* — Yevgeniy Brikman
- The Twelve-Factor App — 12factor.net
- AWS / GCP / Azure official docs and well-architected frameworks

---

## Phase 9 — System Design Case Studies

Work through these end-to-end. Diagram, document tradeoffs, estimate capacity.

**Start here:**

- **Hello Interview — "System Design in a Hurry"** (free, hellointerview.com) — the single best free system design course available. Do this first.

**Classic interview-style designs**

- Design URL shortener (TinyURL / Bitly)
- Design Pastebin
- Design Twitter / X timeline
- Design Instagram / photo-sharing
- Design WhatsApp / chat system
- Design Uber / Lyft (location, matching, pricing)
- Design Netflix / video streaming
- Design YouTube
- Design Dropbox / Google Drive
- Design Google Maps
- Design Yelp / nearby search
- Design Reddit
- Design Notification system
- Design Web crawler
- Design Search autocomplete / typeahead
- Design Distributed file system
- Design Stock exchange / order matching
- Design Ticket booking (BookMyShow, Ticketmaster)
- Design Payment system
- Design Ad click aggregator
- Design Distributed job scheduler
- Design Distributed cache
- Design Rate limiter
- Design Newsfeed system

**Additional resources**

- *System Design Interview Vol 1 & 2* — Alex Xu
- ByteByteGo case studies
- Grokking Modern System Design Interview — Educative (formerly "Grokking the System Design Interview")
- Engineering blogs: Netflix, Uber, Stripe, Discord, Cloudflare, Meta, LinkedIn, Shopify

---

## Distributed Systems Paper Reading List

1. The Google File System (GFS) — Ghemawat et al. (2003)
2. MapReduce — Dean, Ghemawat (2004)
3. Bigtable — Chang et al. (2006)
4. Dynamo — DeCandia et al. (2007)
5. The Chubby Lock Service — Burrows (2006)
6. Paxos Made Simple — Lamport (2001)
7. In Search of an Understandable Consensus Algorithm (Raft) — Ongaro, Ousterhout (2014)
8. Spanner — Corbett et al. (2012)
9. Kafka: a Distributed Messaging System — Kreps et al. (2011)
10. ZooKeeper — Hunt et al. (2010)
11. The Log: What every software engineer should know — Jay Kreps (blog post)
12. Harvest, Yield, and Scalable Tolerant Systems — Fox, Brewer (1999)
13. CAP Twelve Years Later — Eric Brewer (2012)
14. Time, Clocks, and the Ordering of Events — Lamport (1978)
15. Dapper, a Large-Scale Distributed Systems Tracing Infrastructure — Sigelman et al. (2010)

---

## Engineering Blogs to Follow

- Netflix Tech Blog — netflixtechblog.com
- Uber Engineering — eng.uber.com
- Stripe Engineering — stripe.com/blog/engineering
- Discord Engineering — discord.com/blog
- Cloudflare Blog — blog.cloudflare.com
- Meta Engineering — engineering.fb.com
- LinkedIn Engineering — engineering.linkedin.com
- Shopify Engineering — shopify.engineering
- Dropbox Tech — dropbox.tech
- Slack Engineering — slack.engineering
- GitHub Engineering — github.blog/category/engineering
- AWS Architecture Blog — aws.amazon.com/blogs/architecture

---

## Newsletters

- **The Pragmatic Engineer** — Gergely Orosz (architecture decisions at real companies, hiring trends)
- **ByteByteGo Newsletter** — Alex Xu (weekly system design)
- **High Scalability** — archive remains valuable
- **InfoQ** — engineering culture and architecture

---

## YouTube Channels

- ByteByteGo — Alex Xu
- Gaurav Sen
- Asli Engineering by Arpit Bhayani — system design + database internals
- Hussein Nasser — networking, databases, backend
- Jordan Has No Life — system design interviews
- CodeKarle — system design case studies
- TechWorld with Nana — DevOps, Kubernetes

---

## Tools to Get Hands-On With

- **Databases**: PostgreSQL, MySQL, Redis, MongoDB, Cassandra, ClickHouse
- **Messaging**: Kafka, RabbitMQ, NATS
- **Search**: Elasticsearch / OpenSearch
- **Containers**: Docker, Kubernetes
- **Service Mesh**: Istio, Linkerd
- **Observability**: Prometheus, Grafana, Jaeger, OpenTelemetry
- **IaC**: Terraform, Pulumi
- **Cloud**: pick one (AWS / GCP / Azure) and go deep

---

## Progress Log

| Phase | Started | Completed | Notes |
|-------|---------|-----------|-------|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |
| 6 | | | |
| 7 | | | |
| 8 | | | |
| 9 | | | |

## Case Study Log

| Case Study | Date | Notes |
|-----------|------|-------|
| | | |
