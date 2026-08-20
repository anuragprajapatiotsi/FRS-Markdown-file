import re

def replace_diagrams(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. WF-DCP-001
    content = re.sub(
        r'Pillar User\s*\|\s*v\s*Select Pillar.*?Request Sent',
        '''```mermaid
flowchart TD
    A[Pillar User] --> B[Select Pillar]
    B --> C[Select Data Collection Template]
    C --> D[Select Data Provider / Source]
    D --> E[Define Collection Period & Due Date]
    E --> F[Select Submission Method]
    F --> G[Online Form]
    F --> H[Attachment]
    G --> I[Review Request]
    H --> I[Review Request]
    I --> J[Send Data Request]
    J --> K[Email Service]
    K --> L[Data Provider]
    L --> M[Request Sent]
```''',
        content,
        flags=re.DOTALL
    )

    # 2. DIA-DCP-002
    content = re.sub(
        r'Data Ingestion\s*.*?└── Submit',
        '''```mermaid
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
```''',
        content,
        flags=re.DOTALL
    )

    # 3. WF-DCP-002
    content = re.sub(
        r'Data Provider\s*\|\s*v\s*Open Data Collection Request.*?Under Review',
        '''```mermaid
flowchart TD
    A[Data Provider] --> B[Open Data Collection Request]
    B --> C[View Data Collection Template]
    C --> D[Upload Attachment]
    C --> E[Manual Entry]
    C --> F[Online Form]
    D --> G[Validate Submission]
    E --> G
    F --> G
    G --> H{Valid?}
    H -->|Invalid| I[Show Errors]
    H -->|Valid| J[Submit]
    J --> K[Create Data Submission]
    K --> L[Update Request Status]
    L --> M[Under Review]
```''',
        content,
        flags=re.DOTALL,
        count=1
    )

    # 4. DIA-DCP-003
    content = re.sub(
        r'Review & Approve\s*├── Submission Review.*?└── Comments',
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

    # 5. WF-DCP-003
    # Note: Using a slightly different match since Data Provider ... Under Review was used earlier
    content = re.sub(
        r'Data Provider\s*\|\s*v\s*Submit Data\s*\|\s*v\s*Under Review\s*\|\s*v\s*Pillar User.*?Resubmit\s*\|\s*v\s*Under Review',
        '''```mermaid
flowchart TD
    A[Data Provider] --> B[Submit Data]
    B --> C[Under Review]
    C --> D[Pillar User]
    D --> E[Review Submission]
    E --> F[Validate Data]
    F --> G[Approve]
    F --> H[Correction]
    F --> I[Reject]
    G --> J[Approved]
    H --> K[Returned]
    I --> L[Rejected]
    K --> M[Data Provider]
    M --> N[Resubmit]
    N --> C
```''',
        content,
        flags=re.DOTALL
    )

    # 6. DIA-DCP-004
    content = re.sub(
        r'Operational Data Collection Report\s*├── Collection Overview.*?└── Export',
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

    # 7. WF-DCP-004
    content = re.sub(
        r'Pillar User\s*\|\s*v\s*Open Operational Report.*?Optional Export',
        '''```mermaid
flowchart TD
    A[Pillar User] --> B[Open Operational Report]
    B --> C[System Retrieves Collection Data]
    C --> D[Display Collection Status]
    D --> E[Apply Filters]
    D --> F[View Summary]
    E --> G[Filtered Results]
    F --> H[Status Analysis]
    G --> I[Drill Down Request]
    H --> I
    I --> J[View Collection Details]
    J --> K[Optional Export]
```''',
        content,
        flags=re.DOTALL
    )

    # 8. End-to-End
    content = re.sub(
        r'PILLAR USER\s*\|\s*v\s*Configure / Select Template.*?Operational Status Report',
        '''```mermaid
flowchart TD
    A[PILLAR USER] --> B[Configure / Select Template]
    B --> C[Initiate Data Collection]
    C --> D[Send Email Request]
    D --> E[DATA PROVIDER]
    E --> F[Receive Collection Request]
    
    F --> G1[Attachment Upload]
    F --> G2[Manual Entry]
    F --> G3[Online Form]
    
    G1 --> H[Data Validation]
    G2 --> H
    G3 --> H
    
    H -->|Invalid| I1[Correct]
    H -->|Valid| I2[Submit Data]
    
    I2 --> J[UNDER REVIEW]
    J --> K[PILLAR USER]
    K --> L[Review & Validate]
    
    L --> M1[APPROVE]
    L --> M2[RETURN]
    L --> M3[REJECT]
    
    M1 --> N1[APPROVED]
    M2 --> N2[PROVIDER CORRECTION]
    M3 --> N3[REJECTED]
    
    N2 --> O[RESUBMIT]
    O --> J
    
    P[All stages] -.-> Q[Operational Status Report]
```''',
        content,
        flags=re.DOTALL
    )

    # 9. Lifecycle
    content = re.sub(
        r'Draft\s*\|\s*v\s*Sent\s*\|\s*v\s*Pending Submission.*?Resubmitted\s*\|\s*v\s*Under Review',
        '''```mermaid
flowchart TD
    A[Draft] --> B[Sent]
    B --> C[Pending Submission]
    C --> D[Submitted]
    D --> E[Under Review]
    E --> F[Approved]
    E --> G[Returned]
    E --> H[Rejected]
    G --> I[Resubmitted]
    I --> E
```''',
        content,
        flags=re.DOTALL
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

replace_diagrams('Data Collection.md')
