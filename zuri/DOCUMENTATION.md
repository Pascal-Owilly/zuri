+----------------+
|    Person      |
+----------------+
| - id: int      |
| - name: string |
+----------------+

+-----------------+
|   User          |
+-----------------+
      | Uses
      v
+-----------------+
|   API           |
+-----------------+
| - Create        |
| - Read          |
| - Update        |
| - Delete        |
+-----------------+

Client        API
  |            |
  |  Create    |
  |----------->|
  |            |
  |   201 OK   |
  |<-----------|
  |            |

+------------------+
|   API Server     |
+------------------+
|                  |
| - Person API     |
| - Database       |
|                  |
+------------------+

+-------------+        +-------------+
|  Web Client |        |   API Server |
+-------------+        +-------------+
                       |             |
                       | - Person API |
                       | - Database  |
                       +-------------+
