# Scenario 3 Walkthrough: Feature Evolution

## Demo Script

### Setup (30 seconds)
1. Open the `specification.md` file
2. Say to audience: "Let's build a task manager step by step, evolving it based on feedback and new requirements."

### The Demo (6-7 minutes)

#### Iteration 1: Basic Implementation
**What to say**: "Let's start with the simplest possible version."

**Cursor prompt**:
```
Looking at this specification, create a basic task manager that can add and list tasks. Keep it simple - just the core functionality to start.
```

**Expected result**: Simple script with add/list commands and file storage.

#### Iteration 2: Add Task Status
**What to say**: "That works, but we need to mark tasks as complete."

**Cursor prompt**:
```
Enhance the task manager to support marking tasks as complete or incomplete. Add a 'complete' command and show task status when listing.
```

**Show the evolution**: Point out how the code structure adapted to handle status.

#### Iteration 3: Add Due Dates
**What to say**: "Now let's add due dates to make it more useful."

**Cursor prompt**:
```
Add due date functionality. Tasks should optionally have due dates, and we should be able to list tasks sorted by due date. Add a command to add tasks with due dates.
```

**Demonstrate**: Show how the data structure evolved again.

#### Iteration 4: Add Priority Levels
**What to say**: "Let's add priority levels: high, medium, low."

**Cursor prompt**:
```
Add priority levels to tasks (high, medium, low). Update the list command to show priorities and add an option to filter by priority level.
```

#### Iteration 5: Better User Interface
**What to say**: "The command line interface is getting clunky. Let's improve it."

**Cursor prompt**:
```
Improve the user interface. Add colored output for different priorities and statuses. Also add a summary command that shows task counts by status and priority.
```

#### Iteration 6: Data Persistence Improvement
**What to say**: "Let's upgrade from text files to JSON for better data handling."

**Cursor prompt**:
```
Refactor the storage system to use JSON instead of plain text. This will make it easier to handle the complex task data we now have. Include data migration from the old format.
```

### Key Points to Emphasize

1. **Start Simple**: Begin with minimal viable functionality
2. **Incremental Enhancement**: Add one feature at a time
3. **Code Evolution**: Watch how the structure adapts to new requirements
4. **Natural Progression**: Each addition feels like a logical next step
5. **Refactoring**: Code structure improves as complexity grows

### Evolution Demonstrated

1. **Simple text storage** → **Structured data**
2. **Basic commands** → **Rich feature set**
3. **Plain output** → **Formatted, colored display**
4. **Single file** → **Modular architecture**
5. **Text files** → **JSON storage**

### Development Patterns Shown

- **Feature flagging**: Adding optional functionality
- **Data migration**: Upgrading storage formats
- **Interface evolution**: Improving user experience
- **Code organization**: Refactoring for maintainability
- **Backward compatibility**: Preserving existing functionality

### Common Questions and Answers

**Q**: "Do you always know what the next iteration will be?"
**A**: "Not always. Sometimes you discover needs as you use the software. Cursor helps you adapt quickly."

**Q**: "How do you decide when to refactor?"
**A**: "When the code starts feeling messy or when adding new features becomes difficult."

**Q**: "What if you want to change direction completely?"
**A**: "Cursor can help you restructure or even rewrite parts while preserving the working functionality."

### Transition to Next Scenario
"This showed iterative development of a single feature. Now let's see how Cursor helps plan and bootstrap entire projects from scratch." 