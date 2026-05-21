class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        emp_map = {emp.id: emp for emp in employees}
        total_importance = 0
        queue = deque([id])

        while queue:
            curr_id = queue.popleft()
            employee = emp_map[curr_id]
            
            total_importance += employee.importance
            for sub_id in employee.subordinates:
                queue.append(sub_id)
                
        return total_importance
