```mermaid
graph TD
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#ccf,stroke:#333,stroke-width:2px
    style C fill:#cfc,stroke:#333,stroke-width:2px
    style D fill:#fcc,stroke:#333,stroke-width:2px
    style E fill:#ff9,stroke:#333,stroke-width:2px
    style F fill:#ccf,stroke:#333,stroke-width:2px
    style G fill:#cfc,stroke:#333,stroke-width:2px
    style H fill:#f9f,stroke:#333,stroke-width:2px

    A[fa:fa-database BD PostgreSQL] -->|Extrair Dados| B[fa:fa-cogs Orquestração com Airflow]
    B --> C{fa:fa-tachometer-alt Processo de Orquestração}
    C -->|Transferir Dados| D[fa:fa-database Data Warehouse PostgreSQL]
    D --> E[fa:fa-sync Alt Transformação com dbt]
    E --> F[fa:fa-chart-line Criar Dashboard com Power BI]
    
    C -->|Checar Dados| G[fa:fa-check-circle Verificação de Dados]
    F --> H[fa:fa-eye Visualização de Dados]
    
    classDef database fill:#e3f2fd,stroke:#0288d1,stroke-width:2px;
    classDef orchestration fill:#e8f5e9,stroke:#4caf50,stroke-width:2px;
    classDef transformation fill:#fff3e0,stroke:#ff6f00,stroke-width:2px;
    classDef visualization fill:#fbe9e7,stroke:#d32f2f,stroke-width:2px;
    classDef check fill:#f1f8e9,stroke:#388e3c,stroke-width:2px;

    class A,D database;
    class B orchestration;
    class E transformation;
    class F visualization;
    class G check;
