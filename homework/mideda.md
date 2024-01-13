### Quine-McCluskey (QM) Method
1. **Generate prime implicants**
2. **Construct prime implicant table**
3. **Reduce prime implicant table**
    - a. Remove essential prime implicants
    - b. Row dominance
    - c. Column dominance
    - d. Iterate at this step until no further reductions
4. **Solve prime implicant table**

### Heuristic Espresso Method
- **Quine-McCluskey**
    - 隨輸入增加而迅速增加
    - 尋找最小覆蓋是 NP 計算量大
- **Espresso**
    - 暗示不生成主要質數
    - 選擇仍然覆蓋 ON-set 的質數子集
    - 探索覆蓋空間
    - 在相似的精神上在K-map中尋找質數
- **Espresso Algorithm**
    1. EXPAND 
    2. REMOVE-REDUNDANCY
    3. REDUCE
    4. EXPAND
    5. REMOVE-REDUNDANCY
    6. Goto step 3

### Two-Level Logic vs. Multi-Level Logic
**2-Level:**
- f1 = AB + AC + AD
- f2 = AB + AC + AE
    - 不能共享6個產品條款
    - 24 個晶體管在靜態 CMOS 中

**Multi-level:**
- Note that B + C is a common term in f1 and f2
- K = B + C   (3 Levels)
- f1 = AK + AD    (20 transistors in static CMOS)
- f2 = AK + AE    (not counting inverters)


