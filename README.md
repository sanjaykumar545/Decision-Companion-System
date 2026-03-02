# Decision Companion System (CLI)

---

## 1. Understanding of Problem Statement

Real-world decisions often involve multiple competing factors. Whether choosing a bike, laptop, insurance plan, or investment strategy, users face:

- Multiple options  
- Multiple evaluation criteria  
- Trade-offs between factors  
- Uncertainty about what matters most  

Most people make decisions based on emotion, bias, or a single dominant factor (e.g., price or brand).

### Goal of the Project

The goal of this project is to build a **Decision Companion System** that:

- Structures decision-making  
- Quantifies user preferences  
- Evaluates options transparently  
- Provides ranked recommendations  
- Explains the reasoning clearly  

The system must not be a black box and must not rely entirely on AI.

---

## 2. Assumptions Made

- Users can subjectively rate options on a scale (1–10).
- Users can assign importance weights to criteria.
- The user understands their own priorities better than the system.
- Ratings are relative comparisons, not absolute truths.
- The system does not fetch real-time data; it depends on user-provided input.

---

## 3. Why the Solution Was Structured This Way

### Domain-Agnostic Approach

Instead of building a domain-specific system (e.g., only vehicle or insurance), the system was designed as a general decision framework.

**Reason:**  
Most decisions share a common structure:

- Options  
- Criteria  
- Weights  
- Trade-offs  

By abstracting the structure, the system becomes reusable for:

- Buying a bike  
- Choosing a laptop  
- Selecting an insurance plan  
- Evaluating investments  
- Hiring candidates  

---

### Mathematical Model Used

The system uses **Multi-Criteria Decision Analysis (MCDA)** with a weighted normalized scoring model:

```
Score(option) =
( Σ (weight × (rating / max_value)) / total_weight ) × 100
```
Where:

- weight → importance of criterion  
- rating → user score  
- max_value → maximum possible value  
- total_weight → sum of all weights 


#### Why this model?

- Transparent  
- Deterministic  
- Explainable  
- Simple to implement  
- No dependency on AI  
- Efficient for CLI use  

---

## 4. Design Decisions and Trade-offs

### 1️⃣ CLI Instead of Web Application

**Decision:** Implemented as CLI.

**Reason:**

- Focus on logic over UI  
- Faster implementation  
- Lightweight and minimal dependencies  

**Trade-off:**

- Less user-friendly than a GUI  
- No visual charts or dashboards  

---

### 2️⃣ Deterministic Logic Instead of AI-Based Ranking

**Decision:** Use mathematical scoring rather than AI model prediction.

**Reason:**

- Ensures explainability  
- Avoids black-box decisions  
- Meets constraint of not relying entirely on AI  

**Trade-off:**

- Cannot auto-evaluate real-world specifications  
- Depends on user-entered ratings  

---

### 3️⃣ User-Defined Criteria Instead of Predefined Factors

**Decision:** Criteria are dynamic.

**Reason:**

- Increases flexibility  
- Makes system domain-independent  

**Trade-off:**

- User may miss important criteria  

---

### 4️⃣ Weighted Model Instead of Complex Models (AHP / ML)

**Decision:** Use weighted scoring instead of AHP or machine learning.

**Reason:**

- Simpler  
- Transparent  
- Lower computational complexity  
- Easy to explain  

**Trade-off:**

- Does not capture interdependencies between criteria  
- Assumes linear relationships  

---

## 5. Edge Cases Considered

- Equal scores between two options  
  → System handles tie and displays both  

- User enters zero weight for a criterion  
  → That criterion has no impact on the result  

- Very high weight on one criterion  
  → System naturally reflects that priority  

- User changes input  
  → System recalculates dynamically  

- Minimum case:  
  1 option, 1 criterion  
  → Still computes valid output  

---

## 6. How to Run the Project

### Requirements

- Python 3.x installed  

### Steps

Clone repository:

```
git clone https://github.com/sanjaykumar545/Decision-Companion-System
```

Navigate to project folder:

```
cd Decision-Companion-System
```

Run the program:

```
python main.py
```

Follow CLI prompts:

- Enter decision context  
- Enter options  
- Enter criteria, weights and maximum value for the criteria  
- Rate each option with respect to criteria  
- View recommendation  

---

## 7. Example Use Case

### Decision: Buying a Bike

**Options:**

- Royal Enfield Classic 350  
- KTM Duke 200  
- Yamaha R15  

**Criteria and Max-value:**

- Price
- Mileage  
- Power  
- Maintenance Cost  
- Brand Value  

**Rate:**

- Price : For Duke, 150000 
- Likewise, for all other criteria for each option

The system computes:

- Weighted score per option  
- Ranking  
- Explanation of why the top option was recommended  

---

## 8. Explainability

The system explains:

- Which criterion had highest weight  
- Which option performed best in high-weight criteria  
- Trade-offs between options  
- Why the top option scored highest  

This ensures:

- Transparency  
- Trust  
- Interpretability  

---

## 9. What I Would Improve With More Time

- Add sensitivity analysis  
  → Show how ranking changes if weights change  

- Add AI agent api
  → Can fetch values for the options as per criteria

- Add optional AI assistant  
  → Suggest missing criteria
  → Generate more natural explanations  

- Add visualization  
  → Convert to web interface with charts  

- Add persistence  
  → Save past decisions and compare outcomes  


---

## 10. Limitations

- Depends on user-entered ratings
- Different types of criteria for different options is not possible  
- Does not fetch real-world data automatically  
- Assumes linear relationship between weight and rating  
- Does not model probabilistic uncertainty  

---

## 11. Final Reflection

This project demonstrates that structured mathematical reasoning can significantly improve clarity in complex decisions.

Instead of replacing human judgment, the system supports it by:

- Structuring thinking  
- Making trade-offs explicit  
- Providing transparent evaluation  

It is not an AI that decides for the user.  
It is a companion that helps the user decide better.