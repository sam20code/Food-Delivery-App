# Food-Delivery-App
DeliciousBites: A Dynamic Food Delivery App using Django

##**Introduction:**
- In this project, we developed a dynamic and user-friendly food delivery application using Python and the Django framework. The app offers two distinct user roles, namely, an admin with additional privileges to manage food items and users who can view and purchase food items. We implemented various functionalities, including user authentication, adding, updating, and deleting food items, implementing a shopping cart, and handling static files and media contents.
---

##**User Authentication:**

- The application's first page presents users with two options: to log in or sign up as a regular user or as an admin. To ensure secure access, we leveraged Django's built-in authenticate and login libraries, thereby enabling users to access their respective accounts based on their roles.

---
##**Admin Features:**

- Upon logging in as an admin, users are directed to the admin homepage. Here, they have a comprehensive overview of the food items added by them. The navigation bar provides an option to add new items, allowing admins to contribute to the available food choices effortlessly. We utilized Django's forms library to facilitate a user-friendly interface for adding new items. Upon clicking "submit," the newly added item becomes instantly visible on their homepage. Furthermore, admins have the authority to delete existing food items or update their details, enhancing the application's flexibility.

##**User Interface and Shopping Cart:**

- Users accessing the app as regular users are welcomed with an appealing homepage that displays all food items available from various admins. Users have two primary options: to view item details or to make a purchase. To implement this, we designed dynamic URLs that allow users to navigate to individual food item pages and obtain comprehensive details.
---
##**Shopping Cart Implementation:**

- We integrated an efficient shopping cart feature that enables users to add their preferred items and keep track of their selections before finalizing their orders. By skillfully using namespacing and dynamic URLs, we ensured that the cart seamlessly integrates with the rest of the app's functionalities, providing a smooth and intuitive user experience.
---
##**Handling Static Files and Media Contents:**

- To enhance the app's aesthetics, we worked extensively with static files and media contents. Implementing stylesheets, images, and other media components, we ensured a visually pleasing and engaging user interface.
---
##**Conclusion:**

- In conclusion, our food delivery app developed using Python and Django offers a robust and user-friendly platform for both admins and regular users. The clear distinction between admin and user roles, the efficient management of food items, and the seamless implementation of a shopping cart make it a powerful tool for online food delivery services. Through the use of dynamic URLs, namespacing, and various Django libraries, we successfully created an application that delivers a delightful user experience while maintaining security and efficiency.
