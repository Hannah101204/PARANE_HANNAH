import tkinter as tk
from tkinter import ttk, messagebox

def register_user():
    username = username_entry.get()
    password = password_entry.get()

    if not username:
        messagebox.showerror("Error", "Please, enter a username.")
        return
    if not password:
        messagebox.showerror("Error", "Please, enter a password.")
        return

def login_user():
    username = username_entry.get()
    password = password_entry.get()

    if not username:
        messagebox.showerror("Error", "Please, enter a username.")
        return
    if not password:
        messagebox.showerror("Error", "Please, enter a password.")
        return



    if password and username:
        messagebox.showinfo("Login", "Login successful!")
        user_info_window.destroy()
    else:
        messagebox.showerror("Error", "Invalid username or password.")
    return

def open_main_window(user):
    global main_window
    if 'main_window' in globals() and main_window.winfo_exists():
        pass
    else:
        main_window = tk.Tk()
        main_window.title("Habittude - Your Health Companion")
        main_window.geometry("500x300")

        content_frame = tk.Frame(main_window)
        content_frame.pack(pady=20, expand=True)

        window_label = tk.Label(content_frame, text=f"Welcome, {user[1]}!", font='Helvetica 14 bold', fg="#FF1493", wraplength=300)
        window_label.pack(pady=20)

        categories_frame = tk.Frame(content_frame)
        categories_frame.pack(pady=20)

        skincare_button = tk.Button(categories_frame, text="Skincare", command=open_skincare_window, font='Helvetica 10 bold', fg="#ffffff", bg="#FF69B4")
        skincare_button.pack(side=tk.LEFT, padx=10)

        wellbeing_button = tk.Button(categories_frame, text="Mental Wellbeing", command=open_mental_wellbeing_window, font='Helvetica 10 bold', fg="#ffffff", bg="#FF69B4")
        wellbeing_button.pack(side=tk.LEFT, padx=10)

        beauty_tips_button = tk.Button(categories_frame, text="Beauty Tips", command=open_beauty_tips_window, font='Helvetica 10 bold', fg="#ffffff", bg="#FF69B4")
        beauty_tips_button.pack(side=tk.LEFT, padx=10)

        update_account_button = tk.Button(content_frame, text="Update Account", command=lambda: open_update_account_window(user), font='Helvetica 10 bold', fg="#ffffff", bg="#FF1493")
        update_account_button.pack(pady=10)

        logout_button = tk.Button(content_frame, text="Log out", command=main_window.destroy, font='Helvetica 10')
        logout_button.pack(pady=10)

        main_window.mainloop()

def open_skincare_window():
    main_window.withdraw()
    skincare_window = tk.Toplevel(main_window)
    skincare_window.title("Skincare")
    skincare_window.geometry("500x300")
    skincare_window.config(bg="light pink")

    def return_to_main():
        skincare_window.destroy()
        main_window.deiconify()

    return_button = tk.Button(skincare_window, text="Return", font='Helvetica 10 bold', command=return_to_main)
    return_button.pack(pady=10)

    skin_type_var = tk.StringVar(skincare_window)
    skin_type_var.set("Normal")

    skin_type_options = [
        "Normal", "Dry", "Oily", "Combination", "Sensitive"
    ]

    skin_type_dropdown = ttk.Combobox(skincare_window, font='Helvetica 10', textvariable=skin_type_var, values=skin_type_options)
    skin_type_dropdown.pack(pady=5)

    def show_suitable_skincare():
        skin_type = skin_type_var.get()
        if skin_type == "Normal":
            routine_message = """
            *Normal Skin*

            Morning:
            - Cleanse: Use a gentle, hydrating cleanser to remove any overnight buildup.
            - Tone: Apply a toner to balance skin's pH, optional but beneficial.
            - Moisturize: Use a lightweight, oil-free moisturizer to keep skin hydrated.
            - Protect: Apply a broad-spectrum SPF 30 or higher sunscreen.

            Evening:
            - Cleanse: Use a gentle, hydrating cleanser to remove makeup and impurities.
            - Tone: Apply a toner to balance skin's pH, optional but beneficial.
            - Moisturize: Use a lightweight, oil-free moisturizer.

            Recommended products for Normal Skin:
            - Hydrating Lotion.
            - Light Serum.
            """
        
        elif skin_type == "Dry":
            routine_message = """
            *Dry Skin*

            Morning:
            - Cleanse: Use a cream cleanser to avoid stripping natural oils.
            - Tone: Apply a toner to rebalance skin's pH.
            - Treat: Use a hydrating serum with hyaluronic acid to draw in moisture.
            - Moisturize: Apply a rich, hydrating moisturizer.
            - Protect: Apply a broad-spectrum SPF 30 or higher sunscreen.

            Evening:
            - Cleanse: Use a cream cleanser to avoid stripping natural oils.
            - Tone: Apply a toner to rebalance skin's pH.
            - Treat: Use a hydrating serum with hyaluronic acid.
            - Moisturize: Apply a rich, hydrating moisturizer.
            - Optional: Apply a facial oil for extra hydration, especially during colder months.

            Recommended products for Dry Skin: 
            - Moisturizing Cream.
            - Hydrating Mask.
            """

        elif skin_type == "Oily":
            routine_message = """
            *Oily Skin*

            Morning:
            - Cleanse: Use a gel-based cleanser that lathers well to remove oil and debris.
            - Tone: Apply a toner to rebalance skin's pH.
            - Moisturize: Choose a lightweight moisturizer that won't clog pores, avoiding mineral oil and opting for hyaluronic acid or oil-free formulas.
            - Protect: Apply an oil-free, lightweight SPF 30 or higher sunscreen.

            Evening:
            - Cleanse: Double cleanse with an oil-based cleanser followed by a gel-based cleanser to remove makeup and impurities.
            - Tone: Apply a toner to rebalance skin's pH.
            - Treat: Use a salicylic acid or benzoyl peroxide treatment to target acne.
            - Moisturize: Apply a lightweight, oil-free moisturizer.

            Recommended products for Oily Skin:
            - Oil-Free Moisturizer.
            - Mattifying Gel.
            """

        elif skin_type == "Combination":
            routine_message = """
            *Combination Skin (Oily & Dry)*

            Morning:
            - Cleanse: Use a foam cleanser to cleanse both oily and dry areas effectively.
            - Tone: Apply a toner to rebalance skin's pH.
            - Moisturize: Use a lightweight moisturizer for the oily T-zone (forehead, nose, chin) and a heavier moisturizer for the drier areas, or find a product that balances both.
            - Protect: Apply an oil-free, lightweight SPF 30 or higher sunscreen.

            Evening:
            - Cleanse: Double cleanse with an oil-based cleanser followed by a gel-based cleanser to remove makeup and impurities.
            - Tone: Apply a toner to rebalance skin's pH.
            - Treat: Use a mild serum that targets both oily and dry areas.
            - Moisturize: Apply a balanced moisturizer for both oily and dry areas.
            
            Recommended products for Combination Skin:
            - Balanced Moisturizer.
            - Gentle Cleanser.
            """

        elif skin_type == "Sensitive":
            routine_message = """
            *Sensitive Skin*

            Morning:
            - Cleanse: Use a gentle, sulfate-free cleanser with calming ingredients.
            - Tone: Use an alcohol-free toner with soothing ingredients such as chamomile.
            - Moisturize: Use a hypoallergenic moisturizer for sensitive skin.
            - Protect: Apply a broad-spectrum SPF 30 or higher sunscreen with minimal chemical ingredients.

            Evening:
            - Cleanse: Use a gentle cleanser with soothing ingredients.
            - Tone: Apply a soothing toner.
            - Moisturize: Use a calming, anti-inflammatory moisturizer for sensitive skin.
            
            Recommended products for Sensitive Skin:
            - Fragrance-Free Cream. 
            - Soothing Serum.
            """
        
        messagebox.showinfo("Skincare Routine", routine_message)
        return_to_main()

    recommend_button = tk.Button(skincare_window, text="Show Recommendations", command=show_suitable_skincare, font='Helvetica 10 bold', fg="#ffffff", bg="#FF1493")
    recommend_button.pack(pady=10)

def open_mental_wellbeing_window():
    main_window.withdraw()
    mental_wellbeing_window = tk.Toplevel(main_window)
    mental_wellbeing_window.title("Mental Wellbeing")
    mental_wellbeing_window.geometry("500x300")

    def return_to_main():
        mental_wellbeing_window.destroy()
        main_window.deiconify()

    return_button = tk.Button(mental_wellbeing_window, text="Return", font='Helvetica 10 bold', fg="#ffffff", bg="light pink", command=return_to_main)
    return_button.pack(pady=10)

    mood_label = tk.Label(mental_wellbeing_window, text="How are you feeling?", font='Helvetica 10 bold', bg="light pink")
    mood_label.pack(pady=10)

    mood_var = tk.StringVar(mental_wellbeing_window)
    mood_var.set("Stress")

    mood_options = ["Stress", "Anxiety", "Happy", "Sad", "Tired"]
    mood_dropdown = ttk.Combobox(mental_wellbeing_window, font='Helvetica 10', textvariable=mood_var, values=mood_options)
    mood_dropdown.pack(pady=5)

    def show_wellbeing_suggestions():
        mood = mood_var.get()
        if mood == "Stress":
            messagebox.showinfo("Mental Wellbeing Tips", "Take deep breaths, go for a walk, or try some meditation techniques.")
        elif mood == "Anxiety":
            messagebox.showinfo("Mental Wellbeing Tips", "Try deep breathing, journaling, or reaching out to a friend for support.")
        elif mood == "Happy":
            messagebox.showinfo("Mental Wellbeing Tips", "Keep spreading positivity, practice gratitude, and enjoy the moment!")
        elif mood == "Sad":
            messagebox.showinfo("Mental Wellbeing Tips", "Take some time to relax, talk to a loved one, or engage in a hobby you enjoy.")
        elif mood == "Tired":
            messagebox.showinfo("Mental Wellbeing Tips", "Get enough rest, hydrate, and try some relaxation exercises.")
        
        return_to_main()

    wellbeing_button = tk.Button(mental_wellbeing_window, text="Show Suggestions", command=show_wellbeing_suggestions)
    wellbeing_button.pack(pady=10)

def open_beauty_tips_window():
    main_window.withdraw()
    beauty_tips_window = tk.Toplevel(main_window)
    beauty_tips_window.title("Beauty Tips")
    beauty_tips_window.geometry("500x300")

    def return_to_main():
        beauty_tips_window.destroy()
        main_window.deiconify()

    return_button = tk.Button(beauty_tips_window, text="Return", command=return_to_main)
    return_button.pack(pady=10)

    tips_label = tk.Label(beauty_tips_window, text="Beauty Tips for Confidence:", font='Helvetica 10 bold', bg="light pink")
    tips_label.pack(pady=10)

    tips_message = """1. Always smile – It boosts your mood and makes you feel good.\n
    2. Dress in a way that makes you feel comfortable.\n
    3. Take care of your skin.\n
    4. Be kind to yourself – your inner beauty matters too.\n
    5. Surround yourself with positive people.""" 
    
    tips_box = tk.Label(beauty_tips_window, text=tips_message, font='Helvetica 10', bg="light pink", justify="left")
    tips_box.pack(pady=20)

def open_welcome_window():
    welcome_window = tk.Tk()
    welcome_window.title("Welcome to Habittude!")
    welcome_window.geometry("500x300")
    welcome_window.config(bg="light pink")

    welcome_label = tk.Label(welcome_window, text="Welcome to Habittude App, your healthy habit companion!", wraplength=300, font=('Helvetica 20 bold'), bg="light pink")
    welcome_label.pack(pady=20)

    start_button = tk.Button(welcome_window, text="Start", command=lambda: [welcome_window.destroy(), open_user_info_window()], font=('Helvetica 10 bold'), fg="#ffffff", bg="#FF69B4")
    start_button.pack(pady=10)

    welcome_window.mainloop()

def open_user_info_window():
    global user_info_window
    user_info_window = tk.Tk()
    user_info_window.title("Habittude - User Information")
    user_info_window.config(bg="light pink")
    user_info_window.geometry('500x300')

    username_label = tk.Label(user_info_window, text="Username:", font='Helvetica 10 bold', bg="light pink")
    username_label.grid(row=1, column=0, padx=5, pady=5)

    global username_entry
    username_entry = tk.Entry(user_info_window)
    username_entry.grid(row=1, column=1, padx=5, pady=5)

    password_label = tk.Label(user_info_window, text="Password:", font='Helvetica 10 bold', bg="light pink")
    password_label.grid(row=2, column=0, padx=5, pady=5)

    global password_entry
    password_entry = tk.Entry(user_info_window, show="*")
    password_entry.grid(row=2, column=1, padx=5, pady=5)

    register_button = tk.Button(user_info_window, text="Register", command=register_user, font=('Helvetica 10 bold'), fg="#ffffff", bg="#FF69B4")
    register_button.grid(row=4, column=2, pady=10)

    login_button = tk.Button(user_info_window, text="Login", command=login_user, font=('Helvetica 10 bold'), fg="#ffffff", bg="#FF69B4")
    login_button.grid(row=5, column=2, pady=10)

    user_info_window.mainloop()

open_welcome_window()