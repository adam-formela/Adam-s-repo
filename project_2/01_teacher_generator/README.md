## Teacher generator:

The program is a message generator for students that did not submit all assignments in current semester.
Data structure used: function, list.
For this project one module was imported: sys.

Program description:
 - The program gets the data from csv file such as student name, surname, class, missing tasks and grade.
 - The program loads message template from the txt file.
 - For every student (record in the csv file) the program generates message including details about:
   - the current grade,
   - the number of due assignments,
   - the due date,
   - the maximum grade that can be obtained if all overdue projects will be delivered before the due date.