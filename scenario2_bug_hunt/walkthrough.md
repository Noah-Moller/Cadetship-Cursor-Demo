# Scenario 2 Walkthrough: Bug Hunt

## Demo Script

### Setup (30 seconds)
1. Open the `before/data_processor.py` file
2. Show the `test_data.csv` file
3. Say to audience: "This code looks fine at first glance, but it has several bugs. Let me show you how Cursor helps find and fix them."

### The Demo (4-5 minutes)

#### Step 1: Try to run the code
**What to say**: "Let's first try to run this code and see what happens."

**Run command**: 
```bash
cd scenario2_bug_hunt/before
python data_processor.py
```

**Expected result**: The code will crash with an error.

#### Step 2: Ask Cursor to identify bugs
**What to say**: "Instead of debugging manually, let me ask Cursor to analyze this code."

**Cursor prompt**:
```
This Python code has several bugs. Please analyze the data_processor.py file and identify all the issues you can find. For each bug, explain what's wrong and suggest a fix.
```

**Expected response**: Cursor should identify:
1. No null check before using self.data
2. Wrong column name ('cost' vs 'price')
3. Potential division by zero
4. datetime not JSON serializable
5. Missing error handling

#### Step 3: Fix bugs one by one
**What to say**: "Let's fix these bugs systematically."

**Cursor prompt**:
```
Please fix all the bugs you identified in the data_processor.py file. Make sure the code handles edge cases gracefully and includes proper error handling.
```

#### Step 4: Test the fixed code
**What to say**: "Now let's test the fixed version."

**Cursor prompt**:
```
Create a test script that validates our data processor works correctly with the test_data.csv file, including edge cases like missing values and zero quantities.
```

#### Step 5: Add improvements
**What to say**: "While we're at it, let's make the code more robust."

**Cursor prompt**:
```
Add logging throughout the data processor so we can see what's happening at each step. Also add input validation to check file format before processing.
```

### Key Points to Emphasize

1. **Pattern Recognition**: Cursor can spot common bug patterns quickly
2. **Comprehensive Analysis**: It finds multiple issues in a single pass
3. **Fix Suggestions**: Provides specific solutions, not just problem identification
4. **Edge Case Awareness**: Considers scenarios you might miss
5. **Code Quality**: Suggests improvements beyond just fixing bugs

### Types of Bugs Demonstrated

1. **Logic Errors**: Using wrong variable/column names
2. **Runtime Errors**: Division by zero, null references
3. **Type Errors**: JSON serialization issues
4. **Edge Cases**: Empty data, missing values
5. **Error Handling**: Missing try/catch blocks

### Common Questions and Answers

**Q**: "Can Cursor find all types of bugs?"
**A**: "It's excellent at common patterns and logic errors. Complex business logic bugs still need human insight."

**Q**: "How does it compare to traditional debugging?"
**A**: "It's much faster for initial bug identification. You still need to understand the fixes it suggests."

**Q**: "What about performance issues?"
**A**: "Cursor can identify obvious performance problems and suggest optimizations."

### Transition to Next Scenario
"Now that you've seen how Cursor debugs existing code, let's look at how it helps build features iteratively from scratch." 