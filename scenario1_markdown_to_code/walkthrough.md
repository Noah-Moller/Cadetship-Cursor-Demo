# Scenario 1 Walkthrough: Markdown to Code

## Demo Script

### Setup (30 seconds)
1. Open Cursor
2. Open the `specification.md` file
3. Say to audience: "I have a specification for a web scraper. Watch me tell Cursor to implement it."

### The Demo (3-4 minutes)

#### Step 1: Give Cursor the specification
**What to say**: "I'm going to paste this specification and ask Cursor to implement it."

**Cursor prompt**: 
```
Looking at this specification.md file, please implement the complete web scraper as described. Create all necessary files and implement all the requirements.
```

**Expected result**: Cursor should create:
- Main scraper.py file with complete implementation
- Requirements.txt with dependencies 
- Example urls.txt file
- README with usage instructions

#### Step 2: Show the generated code
**What to say**: "Look at what Cursor created. It built the entire scraper based on the specification."

**Point out**:
- Complete class structure
- Error handling implementation
- CSV writing functionality
- Command-line interface
- Proper imports and dependencies

#### Step 3: Test and refine
**What to say**: "Let's test this and see if we need any adjustments."

**Cursor prompt**: 
```
Can you create a sample urls.txt file with a few test URLs and show me how to run this scraper?
```

#### Step 4: Add improvements
**What to say**: "Now let's add a feature that wasn't in the original spec."

**Cursor prompt**:
```
Add functionality to detect and handle different website structures automatically. The scraper should be smart enough to find product information even if the HTML structure varies.
```

### Key Points to Emphasize

1. **Specification Quality**: The more detailed your specification, the better the output
2. **Natural Language**: You can describe requirements in plain English
3. **Complete Implementation**: Cursor builds the entire solution, not just snippets
4. **Iterative Improvement**: You can refine and add features conversationally
5. **Context Awareness**: Cursor understands the domain and makes appropriate choices

### Common Questions and Answers

**Q**: "Does it always work this well?"
**A**: "The quality depends on how clear your specification is. Cursor works best with detailed requirements."

**Q**: "Can it handle more complex projects?"
**A**: "Yes, but for larger projects, you typically break them into smaller specifications and build incrementally."

**Q**: "What if the code has bugs?"
**A**: "That's what our next scenario demonstrates - Cursor is excellent at debugging and fixing issues."

### Transition to Next Scenario
"Now that you've seen how Cursor can generate code from specifications, let's look at how it helps with debugging existing code." 