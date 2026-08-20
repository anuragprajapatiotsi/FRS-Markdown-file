import re

def fix_diagrams(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Fix DIA-DCP-002 and the heading
    # The corrupted part starts at "**4.2.2.2 ```mermaid" and ends at "└── Submit\n\n**D. Ownership"
    content = re.sub(
        r'\*\*4\.2\.2\.2 ```mermaid.*?└── Submit\n\n\*\*D\. Ownership',
        '''**4.2.2.2 Data Ingestion**

**A. Functional Purpose**

The **Data Ingestion** functionality enables the system to receive data submitted by Data Providers through the configured collection mechanism.

The functionality shall support three modes of data ingestion:

1. **Attachment Upload** – Data Provider uploads a completed data file.
2. **Manual Entry** – Authorized user enters data directly into the application.
3. **Online Form Submission** – Data Provider submits data through the online form.

The system shall validate the submitted data against the configured Data Collection Template and maintain the submission against the corresponding Data Collection Request.

**B. Business Definitions**

| **Term** | **Definition** |
| --- | --- |
| Data Submission | Data submitted against a Data Collection Request. |
| Manual Entry | Direct entry of required data into application fields by an authorized user. |
| Attachment Upload | Upload of a file containing requested data. |
| Online Form Submission | Submission of data through a system-generated online form. |
| Validation | System-based verification of data format, completeness and configured business rules. |
| Submission Status | Current state of a submitted data package. |
| Data Source | Source/entity from which the data originates. |

**C. Functional Hierarchy Diagram**

**Diagram type:** Functional hierarchy diagram  
**Diagram ID:** DIA-DCP-002

```mermaid
flowchart TD
    A[Data Ingestion]
    A --> B[Attachment Upload]
    B --> B1[Select File]
    B --> B2[Upload File]
    B --> B3[File Validation]
    B --> B4[Data Validation]
    
    A --> C[Manual Entry]
    C --> C1[Open Data Form]
    C --> C2[Enter Data]
    C --> C3[Field Validation]
    C --> C4[Submit]
    
    A --> D[Online Form Submission]
    D --> D1[Open Form]
    D --> D2[Enter Data]
    D --> D3[Validate Data]
    D --> D4[Submit]
```

**D. Ownership''',
        content,
        flags=re.DOTALL
    )

    # Replace DIA-DCP-003
    content = re.sub(
        r'Review & Approve\n\n│\n\n├── View Submitted Data.*?└── Comments',
        '''```mermaid
flowchart TD
    A[Review & Approve]
    A --> B[Submission Review]
    B --> B1[Open Submission]
    B --> B2[View Data]
    B --> B3[View Attachments]
    
    A --> C[Data Validation]
    C --> C1[Check Completeness]
    C --> C2[Verify Business Rules]
    
    A --> D[Review Decision]
    D --> D1[Reviewer]
    D --> D2[Review Date/Time]
    D --> D3[Decision]
    D3 --> D3a[Approve]
    D3 --> D3b[Return for Correction]
    D3 --> D3c[Reject]
    D --> D4[Comments]
```''',
        content,
        flags=re.DOTALL
    )

    # Replace DIA-DCP-004
    content = re.sub(
        r'Operational Data Collection Report\n\n│\n\n├── Collection Overview.*?└── Export',
        '''```mermaid
flowchart TD
    A[Operational Data Collection Report]
    A --> B[Collection Overview]
    B --> B1[Total Requests]
    B --> B2[Submitted]
    B --> B3[Pending]
    B --> B4[Under Review]
    B --> B5[Approved]
    B --> B6[Returned]
    B --> B7[Rejected]
    
    A --> C[Collection Progress]
    C --> C1[By Pillar]
    C --> C2[By Data Provider]
    C --> C3[By Collection Period]
    
    A --> D[Overdue Monitoring]
    D --> D1[Overdue Requests]
    D --> D2[Upcoming Due Dates]
    
    A --> E[Report Actions]
    E --> E1[Filter]
    E --> E2[Search]
    E --> E3[View Details]
    E --> E4[Export]
```''',
        content,
        flags=re.DOTALL
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

fix_diagrams('Data Collection.md')
