# event_management_API
Practical Task:
Building a simplified event management API for an admin panel. It should support role-based access (Admin and User), event creation, and basic ticket purchases.

Requirements:

1. Set up Django Project:

	Create a Django project called EventAPI.
	Use PostgreSQL or MySQL for the database.

2. Models:

	User:
	id: Primary Key
	username: CharField (Unique)
	password: CharField (Hashed)
	role: Choices (Admin, User)
	Event:
	id: Primary Key
	name: CharField (Max 255 characters)
	date: DateField
	total_tickets: IntegerField
	tickets_sold: IntegerField (default 0)
	Ticket:
	id: Primary Key
	user: ForeignKey to User
	event: ForeignKey to Event
	quantity: IntegerField (Number of tickets purchased)
	purchase_date: DateTimeField (auto_now_add=True)

3. API Endpoints (with Role-based Access):

	User Registration:
		POST /api/register/ - Register a user (Admin/User).
	
Event Management (Admin Only):
	POST /api/events/ - Create a new event (Admin only).
	GET /api/events/ - Fetch all events (Admin and User).

	Ticket Purchase (User Only):
	POST /api/events/{id}/purchase/ - Purchase tickets for an event.
	Request Body: { "quantity": <number_of_tickets> }

	Before completing the purchase, the system should:
	Check if the quantity requested plus tickets_sold is less than or equal to total_tickets.
	If valid, create an entry in the Ticket table with the specified quantity.
	Update the tickets_sold field in the Event model accordingly.
	Return an error if the purchase would exceed the available tickets.

4. SQL Query:

	Write a custom SQL query to fetch the total tickets sold for all events along with event details. The query should optimize for large datasets and return the top 3 events by tickets sold.

5. Validation:

	Ensure that the ticket quantity requested does not exceed available tickets (tickets_sold + quantity must not exceed total_tickets).
	Return appropriate error messages for invalid purchase requests (e.g., trying to purchase more tickets than are available or purchasing for a non-existent event).

Bonus (Optional):

	Implement basic JWT-based authentication for login.

Deliverables:

	Codebase (Django project).
	A sample custom SQL query for fetching ticket sales.
	Well-commented code explaining the key logic, particularly around ticket purchases and SQL queries.

Submission: 
Share the code repository (GitHub, GitLab, etc.) containing the source code along with a README file explaining. Make sure it's publicly accessible. Additionally, you can include any thoughts or considerations about implementation.

