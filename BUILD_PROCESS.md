Problem Statement : Decision Companion System

Initially, I considered developing a subject-specific decision companion system focused on vehicle selection. As a young adult, purchasing a vehicle is often the first major financial decision, and confusion typically arises due to multiple factors such as budget, mileage, brand, and performance.

However, upon deeper reflection, I realized that such a system would primarily serve a specific demographic (youth) and would lack broader applicability.

To widen the scope, I researched common areas where humans face decision confusion. Through references and observation, I identified domains such as:

- Relationships  
- Careers  
- Health  
- Financial Planning  

This led me to explore a **health insurance companion system**. During research, I discovered that insurance includes multiple categories and subcategories, each requiring detailed domain knowledge and updated policy information. This made the system domain-heavy and only occasionally useful.


Next, I explored building a **secondary investment companion system** to help users choose between stocks, bonds, and mutual funds.

However, this approach required:

- Real-time data tracking  
- Market trend analysis  
- Risk modeling  
- Machine learning predictions  

Given the constraints of the assignment (no heavy AI reliance and no external monitoring), this approach was impractical.


After further reflection, I identified a key insight:

> All decision problems, regardless of domain, share a common structure.

They typically involve:

- Multiple options  
- Multiple evaluation criteria  
- Different importance levels  
- Trade-offs between factors  


Instead of building a domain-specific system, I decided to design a **domain-agnostic decision framework**.

The system uses weighted scoring based on **Multi-Criteria Decision Analysis (MCDA)**:

```
Score = Σ(weight × rating)
```

This approach was selected because it is:

- Transparent  
- Deterministic  
- Explainable  
- Computationally simple  
- Independent of AI  

To simplify implementation and focus on decision logic rather than interface design, the system was implemented as a **CLI application**.

This final design ensures:

- Flexibility across domains (bike, laptop, investment, etc.)  
- Dynamic user input  
- Transparent reasoning  
- Compliance with assignment constraints  