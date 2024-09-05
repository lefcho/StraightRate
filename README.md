# Straight Rate

Straight Rate is a website that allows users to create profiles and rate movies and video games.

## Key Features

- **User Profiles:** Create a profile to start rating movies and video games.
- **Django 5.2:** Developed using Django.
- **PostgreSQL Database:** Using PostgreSQL with psycopg2.
- **Pillow:** Image processing for saving posters of movies and video games.

---

## Website Flow

### Homepage

- **Displays the top 5 rated movies and video games:** "Get out" is hovered.

  ![Homepage Screenshot](https://github.com/user-attachments/assets/23aa3f91-6ac0-45d1-8351-cc65c97b7408)

### Movies Dashboard

- **View Movies:** Displays a list of movies available for rating.

  ![Movies Dashboard Screenshot](https://github.com/user-attachments/assets/010ca7fd-0bda-40c8-9ca0-62bb5d2654f9)

### Video Games Dashboard

- **View Video Games:** Displays a list of video games available for rating.

  ![Video Games Dashboard Screenshot](https://github.com/user-attachments/assets/fbe36044-f404-4ed7-88e4-e9e58f94aa8b)

### Search Bar

- **Expandable Search bar:** The search bar expands when the magnifying glass is clicked or focused.
- **Search Button:** The circle at the end serves as a confirm search button.

  ![Search Bar Screenshot](https://github.com/user-attachments/assets/7dc98bdd-31b2-4420-98aa-33c4b22eabbf)

### Search Results

- **Display Results:** Shows the movies or video games matching the search query.

  ![Search Results Screenshot](https://github.com/user-attachments/assets/7e7be978-4681-4988-9caf-c2495b5ec4c9)

### Create an Account

- **User Registration:** Sign up to start rating movies and video games.

  ![Create Account Screenshot](https://github.com/user-attachments/assets/d17fa30e-6873-4568-9f4c-3608a6268019)

### Log in

- **User Authentication:** Log in to your account.

  ![Login Screenshot](https://github.com/user-attachments/assets/50ada4a4-2352-4935-b5d6-414513dd65f6)

### View Profile

- **Profile Page:** Displays the user's profile, including their reviews.
- **Edit Reviews:** Clicking on a movie/video game title under "My Reviews" takes you to that page to edit your review.

  ![View Profile Screenshot](https://github.com/user-attachments/assets/76c1e744-d889-4e15-a065-8b6c9433d286)

### Edit Profile

- **Optional Fields:** First and last names are optional when creating a profile, but can be added later.
- **Unlock Fields:** Clicking on the "Edit Profile" button unlocks the fields for editing.
- **Save/Cancel:** Saving or canceling locks the fields again.

  ![Edit Profile Screenshot](https://github.com/user-attachments/assets/6eeb49b3-12b3-4e65-9703-cc21498dd8f3)

### Movie/Video Game Details (Not Logged In)

- **View Details:** Displays detailed information about a movie or video game without requiring a login.

  ![Movie Details Not Logged In Screenshot](https://github.com/user-attachments/assets/fa9d43eb-ce26-46a4-9bd3-6282983b604d)

### Movie/Video Game Details (Logged In, No Review Yet)

- **Leave Review:** Allows logged-in users to leave a review if they haven't already.

  ![Leave Review Screenshot](https://github.com/user-attachments/assets/83bb674c-3bb6-4fec-ac4e-4881bd0c6253)

  - **Leave Review Button Pressed:** The review form appears.

    ![Leave Review Button Pressed Screenshot](https://github.com/user-attachments/assets/c97340b9-daa0-40df-a0b1-59c30cabd39e)

### Movie/Video Game Details (Logged In and Reviewed)

- **Edit Review:** Logged-in users who have already reviewed can edit their reviews.

  ![Edit Review Screenshot](https://github.com/user-attachments/assets/fad3ce99-61f2-4305-ad49-5f1757b7d1cf)

  - **Edit Review Button Clicked:** The stars and comment fields unlock for editing.
  - **Save/Cancel:** Saving or canceling locks the fields again.

    ![Edit Review Button Clicked Screenshot](https://github.com/user-attachments/assets/8b660e41-fca9-4db1-9218-6d6a5ecc4169)
