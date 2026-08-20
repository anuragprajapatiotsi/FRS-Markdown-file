import re

def replace_dia_dcp_001(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The image is after **Diagram:** and before **D. Ownership
    replacement = """**Diagram:**

```mermaid
flowchart TD
    A[DATA COLLECTION PROCESS] --> B[INITIATE DATA COLLECTION]
    B --> C[SELECT PILLAR]
    C --> D[SELECT DATA COLLECTION TEMPLATE]
    D --> E[DATA COLLECTION PERIOD]
    E --> F[DEFINE DUE DATE]
    F --> G[SELECT SUBMISSION METHOD]
    
    G --> G1[ONLINE FORM]
    G --> G2[ATTACHMENT]
    
    G --> H[REVIEW REQUEST]
    H --> I[SEND EMAIL]
    I --> J[TRACK REQUEST STATUS]
    
    J --> J1[DRAFT]
    J --> J2[SENT]
    J --> J3[OPENED]
    J --> J4[SUBMITTED]
    J --> J5[UNDER REVIEW]
    J --> J6[APPROVED]
    J --> J7[REJECTED]
```

**D. Ownership"""
    
    content = re.sub(
        r'\*\*Diagram:\*\*\s*\n\n!\[\]\(data:image/png;base64,.*?\)\n\n\*\*D\. Ownership',
        replacement,
        content,
        flags=re.DOTALL
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

replace_dia_dcp_001('Data Collection.md')
