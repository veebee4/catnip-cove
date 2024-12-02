# **Catnip Cove**

![amiresponsive mock-ups of Catnip Cove]

**[Link to the Deployed Site]**

![GitHub last commit]
![GitHub language count]
![GitHub top language] - go to shields.io

# Project Overview

Catnip Cove is a fictitious cat rescue centre, ecommerce full stack donation project built using Django, Python, JavaScript and Bootstrap. The site is deployed to Heroku, which uses Stripe for payment processing.

Catnip Cove is my 4th milestone project for Code Institute's Level 5 Diploma in Web Application Development (Full Stack Software Development).
<br/>

---

**TABLE OF CONTENTS**
* [USER EXPERIENCE](#user-experience)
    * [Strategy Plane](#strategy-plane)
        * [Project Goals](#project-goals)
    * [Scope Plane](#scope-plane)
        * [Feature Planning](#feature-planning)
        * [Content Requirement Planning](#content-requirement-planning)
            * [Content Type: Text](#content-type-text)
            * [Content Type: Images](#content-type-images)
            * [Content Type: Videos](#content-type-videos)
            * [Integrating Content Strategy and SEO](#integrating-content-strategy-and-seo)
        * [User Stories](#user-stories)
    * [Structure Plane](#structure-plane)
        * [Interaction Design](#interaction-design)
            * [User Flow Diagram](#user-flow-diagram)
        * [Information Architecture](#information-architecture)
            * [Site Map](#site-map)
        * [Database Design](#database-design)
            * [Database ERD](#database-erd)
            * [Data Modelling](#data-modelling)
                * [User Model](#user-model)
                * [UserProfile](#userprofile-model)
                * [MainCategory Model](#maincategory-model)
                * [Category Model](#category-model)
                * [Subcategory Model](#subcategory-model)
                * [Brand Model](#brand-model)
                * [Product Model](#product-model)
                * [Order Model](#order-model)
                * [OrderLineItem Model](#orderlineitem-model)
                * [Review Model](#review-model)
                * [Wishlist Model](#wishlist-model)
    * [Skeleton Plane](#skeleton-plane)
        * [Wireframes](#wireframes)
    * [Surface Plane](#surface-plane)
        * [Typography](#typography)
        * [Colour Palette](#colour-palette)
        * [Imagery](#imagery)
* [Agile Methodology](#agile-methodology)
    * [GitHub Projects](#github-projects)
* [Features](#features)
    * [Product Categorization](#product-categorization)
    * [Stock Keeping Unit (SKU) Architecture](#stock-keeping-unit-sku-architecture)
    * [Defensive Programming](#defensive-programming)
    * [Accessibility](#accessibility)
    * [Extra Meta Tags for Specific Pages](#extra-meta-tags-for-specific-pages)
    * [Multi Brands](#multi-brands)
    * [Brand Management - Authorized Personnel Only](#brand-management---authorized-personnel-only)
    * [Product Management - Authorized Personnel Only](#product-management---authorized-personnel-only)
    * [Product Reviews](#product-reviews)
    * [Related Products](#related-products)
    * [Wishlist](#wishlist)
    * [Site Features Common to All Pages](#site-features-common-to-all-pages)
    * [Site Pages](#site-pages)
* [Future Development, Iteration and Implementation](#future-development-iteration-and-implementation)
* [Technologies Used](#technologies-used)
    * [Languages Used](#languages-used)
    * [Frameworks Used](#frameworks-used)
    * [Databases Used](#databases-used)
    * [Libraries and Packages Used](#libraries-and-packages-used)
    * [Programmes and Applications Used](#programmes-and-applications-used)
    * [Payment Processing Platform Used](#payment-processing-platform-used)
    * [Cloud Application Platforms Used](#cloud-platforms-used)
    * [Cloud Storage Services Used](#cloud-storage-services-used)
* [Testing](#testing)
* [Bugs, Issues and Solutions](#bugs-issues-and-solutions)
* [Deployment and Local Development](#deployment-and-local-development)
    * [Deployment](#deployment)
    * [Local Development](#local-development)
        * [How to Fork](#how-to-fork)
        * [How to Clone](#how-to-clone)
* [Credits](#credits)
* [Acknowledgements](#acknowledgements)

---

# User Experience

## STRATEGY PLANE

Cat rescue centres are hardworking charities that employ numerous staff, including volunteers and require donations to continue the work that they do. From helping strays to struggling families with household pet cats.
They have even helped people who are in a domestic abuse situation within their living space, by taking in pets to help and make it easier for the victims to get away from the situation they are in without worrying about their pets.
They require all the help they can get, from anyone.

### **Project Goals**

My goal is to create a website that allows users to donate money to the rescue centre, to keep track of how much they have donated and to have information about the cats at the rescue and cats in general by way of a blog.

## SCOPE PLANE
### **Feature Planning**
<!-- When planning the Shop K-Beauty ecommerce store's features and scope, I drew up a Desirability, Importance and  Viability analysis of all the possible features to be included in the project, ranking them by order of importance from low (1) to high (5). Features that ranked the highest will be prioritised and should they have been delivered within this release, will then be marked accordingly so. The target users for each ranked feature are also identified.

| # | Feature | Target User | Desirability | Importance | Viability  | Delivered |
| --- | --- | --- | --- | --- | --- | --- |
| User Accounts |  |  |  |  |  |  |
| 1 | User Role Permissions | All Users <sup>1</sup> | 5 | 5 | 5 | ✅ |
| 2 | Account Registration | All Users <sup>1</sup> | 5 | 5 | 5 | ✅ |
| 3 | User Email Confirmation | All Users <sup>1</sup> | 5 | 5 | 5 | ✅ |
| 4 | Password Reset | All Users <sup>1</sup> | 5 | 5 | 5 | ✅ |
| 5 | Social Media Registration &amp; Login | Visitors &amp; Shoppers | 5 | 2 | 2 | ❌ |
| 6 | User Profile Page | Registered Users | 5 | 5 | 5 | ✅ |
| Navigation |  |  |  |  |  |  |
| 7 | Top Navigation to include: logo, search bar, my account (register, login) and bag | All Users <sup>1</sup> | 5 | 5 | 5 | ✅ |
| 8 | Top Navigation to include: my account (my profile, logout), wishlist | Logged In Users | 5 | 5 | 5 | ✅ |
| 9 | Top Navigation Search Bar: to be enabled for product name, brands or ingredients searching | All Users <sup>1</sup> | 5 | 5 | 5 | ✅ |
| 10 | Top Navigation to include: my account (brand management, product management, my profile, logout) and wishlist | Logged In Shop Owners &amp; Superadmins | 5 | 5 | 5 | ✅ |
| 11 | Main Navigation to include links to: all products, product types by categories, special offers and available brands | All Users <sup>1</sup> | 5 | 5 | 5 | ✅ |
| Products |  |  |  |  |  |  |
| 12 | Featured Products | All Users <sup>1</sup> | 5 | 5 | 5 | ✅ |
| 13 | Product Main Categories | All Users <sup>1</sup> | 5 | 5 | 5 | ✅ |
| 14 | Product Categories | All Users <sup>1</sup> | 5 | 5 | 5 | ✅ |
| 15 | Product Subcategories | All Users <sup>1</sup> | 5 | 5 | 5 | ✅ |
| 16 | Product Detail page to include: link to brands, categories and subcategories, accordion to contain description, how to use and ingredient details | All Users <sup>1</sup> | 5 | 5 | 5 | ✅ |
| 17 | Product Subcategories | All Users <sup>1</sup> | 5 | 5 | 5 | ✅ |
| 18 | Randomized List of Related Products (filtered by subcategory) | All Users <sup>1</sup> | 5 | 4 | 3 | ✅ |
| 19 | Product Management - Create, Read, Update and Delete Products via the front-end | Shop Owners &amp; Superadmins | 5 | 5 | 5 | ✅ |
| Brands |  |  |  |  |  |  |
| 20 | Featured Brands | All Users <sup>1</sup> | 5 | 5 | 5 | ✅ |
| 21 | List of All Available Brands | All Users <sup>1</sup> | 5 | 5 | 5 | ✅ |
| 22 | List of All Available Products by Brand | All Users <sup>1</sup> | 5 | 5 | 5 | ✅ |
| 23 | Brand Management - Create, Read, Update Brands via the front-end | Shop Owners &amp; Superadmins | 5 | 5 | 5 | ✅ |
| Stock Inventory |  |  |  |  |  |  |
| 24 | Display Percentage of Stock Availability against Total Quantity of Stocks Per Product  | All Users <sup>1</sup> | 3 | 3 | 3 | ❌ |
| 25 | Automatically Deduct quantity of product sold from Total Quantity and Update Stock Availability Displayed on Product Detail Page | All Users <sup>1</sup> | 4 | 2 | 2 | ❌ |
| 26 | Design SKUs to Conform with both Stock Inventory and Pick and Pack Fulfillment <sup>2</sup> | Shop Owners &amp; Superadmin | 5 | 5 | 5 | ✅ |
| Checkout |  |  |  |  |  |  |
| 27 | Email Confirmation of Order | Shoppers | 5 | 5 | 5 | ✅ |
| 28 | Order History | Shoppers | 5 | 5 | 5 | ✅ |
| 29 | Save/ Update Customer Details on Checkout | Shoppers | 5 | 5 | 5 | ✅ |
| Product Reviews |  |  |  |  |  |  |
| 30 | Product Reviews - Create and Read Reviews | Logged In Users  |  5 | 5 | 5 | ✅ |
| 31 | Product Reviews - Create, Read Update and Delete Reviews | Shop Owners and Superadmins (CRUD) |  5 | 5 | 5 | ✅ |
| Wishlist |  |  |  |  |  |  |
| 32 | Individual User's Wishlist - Create, Read, Update and Delete Wishlist | Logged In Users | 5 | 5 | 5 | ✅ |
| 33 | Policy Pages | All Users <sup>1</sup> | 5 | 5 | 5 | ✅ |
| Digital Marketing |  |  |  |  |  |  |
| 34 | Social Media Presence | Shop Owners &amp; Superadmins | 5 | 5 | 5 | ✅ |
| Email Marketing |  |  |  |  |  |  |
| 35 | Email Subscription, Powered by MailChimp | Registered Subscribers | 3 | 3 | 3 | ❌ |
| Contact Us |  |  |  |  |  |  |
| 36 | Contact Form | All Users <sup>1</sup> | 3 | 3 | 3 | ❌ |
| Loyalty, Gift Cards and Discount Vouchers |  |  |  |  |  |  |
| 37 | Loyalty Cards | Shoppers | 4 | 3 | 2 | ❌ |
| 38 | Digital Gift Cards | All Users <sup>1</sup> | 5 | 2 | 1 | ❌ |
| 39 | Digital Discount Vouchers | All Users <sup>1</sup> | 5 | 2 | 1 | ❌ |
| Other Features |  |  |  |  |  |  |
| 40 | SEO Friendly URLs - use slugs for URLs vs IDs such as product id, review id, brand id for better SEO | All Users <sup>1</sup> | 3 | 5 | 2 | ❌ |

1. All Users: Site Visitors, Logged In Users, Shop Owners, Superadmins

2. Source: [James and James Ecommerce Fulfillment: What is SKU and how are they used by retailers?](https://www.ecommercefulfilment.com/en/scale-up/sku-important-many-need/) -->

### **User Stories**
<!-- | **USER STORY #** | **ISSUE ID** | **As a/an** | **I want to be able to...** | **So that I can...** |
| --- | --- | --- | --- | --- |
| **VIEWING & NAVIGATION** |   |   |
| 1 | [#9](https://github.com/JoyZadan/shop-kbeauty/issues/9) | Shopper | Navigate around the site | View a list of products  |
| 2 | [#54](https://github.com/JoyZadan/shop-kbeauty/issues/54) | Shopper | View a specific category of products | Quickly find products I'm interested in without having to search through all products. |
| 3 | [#47](https://github.com/JoyZadan/shop-kbeauty/issues/47) | Shopper | Quickly identify deals, clearance items and special offers | Take advantage of special savings on products I'd like to purchase |
| 4 | [#32](https://github.com/JoyZadan/shop-kbeauty/issues/32) | Shopper | Quickly view how much was the original price | Identify how much I may be able to save when buying the product and may also help me compare prices with other sites |
| 5 | [#36](https://github.com/JoyZadan/shop-kbeauty/issues/36) | Shopper | View individual product details | Identify the price, description, product reviews, product image, product ingredients and instructions how to use product |
| 6 | [#38](https://github.com/JoyZadan/shop-kbeauty/issues/38) | Shopper | Easily view the total amount of products in my shopping bag at any time throughout my visit | Avoid spending too much |
| 7 | [#28](https://github.com/JoyZadan/shop-kbeauty/issues/28) | Shopper | Easily view the featured brands | To assure me that Shop K-Beauty really offers K-Beauty products from authentic K-Beauty brands |
| 8 | [#48](https://github.com/JoyZadan/shop-kbeauty/issues/48) | Shopper | Search/ View all of the available K-Beauty brands | Look for my favourite brands  |
| 9 | [#70](https://github.com/JoyZadan/shop-kbeauty/issues/70) | Shopper | Easily view details about the brand of a product I am purchasing | Learn more about the brands and feel confident about my purchase |
| 10 | [#73](https://github.com/JoyZadan/shop-kbeauty/issues/73) | Shopper | View a list of available products when viewing the details about a brand | Quickly decide what product to purchase from a particular brand |
| 11 | [#81](https://github.com/JoyZadan/shop-kbeauty/issues/81) | Shopper | Find skincare tips and information about K-Beauty skincare routine | Decide which products I need to purchase |
| 12 | [#82](https://github.com/JoyZadan/shop-kbeauty/issues/82) | Shopper | Easily navigate from a product category to the corresponding subcategories | Easily find the products I am looking for |
| 13 | [#89](https://github.com/JoyZadan/shop-kbeauty/issues/89) | Shopper | View Related products | Make a more informed decision before finalising my purchase |
| **REGISTRATION & USER ACCOUNTS** |   |   |
| 14 | [#8](https://github.com/JoyZadan/shop-kbeauty/issues/8)| Shopper | Easily register for an account | Have a personal account and be able to view my profile |
| 15 | [#52](https://github.com/JoyZadan/shop-kbeauty/issues/52) | Shopper | Receive an email confirmation after registering | View that my personal account registration was successful |
| 16 | [#50](https://github.com/JoyZadan/shop-kbeauty/issues/50) | Shopper | Easily login and logout of my shopper's account | Access my personal account information |
| 17 | [#51](https://github.com/JoyZadan/shop-kbeauty/issues/51) | Shopper | Easily recover my password in case I forget it | Recover access to my account |
| 18 | [#53](https://github.com/JoyZadan/shop-kbeauty/issues/53) | Shopper | Have a personalised user profile | View my personal order history and order confirmations |
| **SORTING & SEARCHING** |   |   |
| 19 | [#31](https://github.com/JoyZadan/shop-kbeauty/issues/31) | Shopper | Sort the list of available products | Easily identify the best priced, best discounted products and categorically and subcategorically sorted products |
| 20 | [#54](https://github.com/JoyZadan/shop-kbeauty/issues/54) | Shopper | Sort a specific category of product | Find the best priced product in a specific category |
| 21 | [#55](https://github.com/JoyZadan/shop-kbeauty/issues/55) | Shopper | Sort a specific subcategories of products | To easily identify the most suitable product for me to purchase |
| 22 | [#56](https://github.com/JoyZadan/shop-kbeauty/issues/56) | Shopper | Sort multiple categories of products simultaneously | Find the best priced products or discounts across broad categories, such as "skincare" or "hair &amp; body" |
| 23 | [#29](https://github.com/JoyZadan/shop-kbeauty/issues/29) | Shopper | Search for a product or products by name, by description or by ingredients | Find a specific product I'd like to purchase  |
| 24 | [#57](https://github.com/JoyZadan/shop-kbeauty/issues/57) | Shopper | Easily see what I've searched for and the number of results | Quickly decide whether the product I want is available |
| **PURCHASING & CHECKOUT** |   |   |
| 25 | [#32](https://github.com/JoyZadan/shop-kbeauty/issues/32) | Shopper | Quickly view how much was the original price and what savings, if any are available | Easily compare prices with other sites |
| 26 | [#39](https://github.com/JoyZadan/shop-kbeauty/issues/39) | Shopper | Easily select the quantity for a product when purchasing it | Ensure I don't accidentally select the wrong product quantity |
| 27 | [#33](https://github.com/JoyZadan/shop-kbeauty/issues/33) | Shopper | Easily view notifications on screen when I add a product to my bag | Find out immediately if my actions were correct or if the was an error |
| 28 | [#40](https://github.com/JoyZadan/shop-kbeauty/issues/40) | Shopper | View items in my bag to be purchased | Identify the total cost of my purchase and all items I will receive |
| 29 | [#41](https://github.com/JoyZadan/shop-kbeauty/issues/41) | Shopper | Adjust the quantity of individual items in my bag | Easily make changes to my purchase before checkout |
| 30 | [#42](https://github.com/JoyZadan/shop-kbeauty/issues/42) | Shopper | Easily enter my payment information | Check out quickly and with no hassles |
| 31 | [#43](https://github.com/JoyZadan/shop-kbeauty/issues/43) | Shopper | Feel my personal and payment information is safe and secure | Confidently provide the needed information to make a purchase |
| 32 | [#44](https://github.com/JoyZadan/shop-kbeauty/issues/44) | Shopper | View an order confirmation after checkout | Verify that I haven't made any mistakes |
| 33 | [#45](https://github.com/JoyZadan/shop-kbeauty/issues/45) | Shopper | Receive an email confirmation after checking out | Keep the confirmation of what I've purchased for my records |
| **PRODUCT REVIEWS** |   |   |
| 34 | [#64](https://github.com/JoyZadan/shop-kbeauty/issues/64) | Shopper | View available reviews for a product I am viewing  | Find out what others think of the product |
| 35 | [#58](https://github.com/JoyZadan/shop-kbeauty/issues/58) | Shopper | Easily see how I can add my reviews on products I purchased | Decide whether I want to add my review |
| 36| [#71](https://github.com/JoyZadan/shop-kbeauty/issues/71) | Shopper | Easily view/ have access to details about the product I am reviewing | Refer to the information about the product, should I need to do so |
| 37 | [#65](https://github.com/JoyZadan/shop-kbeauty/issues/65) | Shopper | Add my review of the product | Share my personal experience of using the products |
| 38 | [#23](https://github.com/JoyZadan/shop-kbeauty/issues/23) | Store Owner | Add Featured Reviews on specific product detail page | Opt to highlight specific reviews |
| 39 | [#66](https://github.com/JoyZadan/shop-kbeauty/issues/66) | Store Owner | Edit submitted reviews | Opt to block off profanities, if any |
| 40 | [#67](https://github.com/JoyZadan/shop-kbeauty/issues/67) | Store Owner | Delete a review | Have control over unacceptable comments such as discriminatory statements, if any |
| **ADMIN & STORE MANAGEMENT** |   |   |
| 41 | [#60](https://github.com/JoyZadan/shop-kbeauty/issues/60) | Store Owner | Add a product | Add new items to my store |
| 42 | [#61](https://github.com/JoyZadan/shop-kbeauty/issues/61) | Store Owner | Edit/update a product | Change product process, descriptions, ingredients, images and other product criteria |
| 43 | [#62](https://github.com/JoyZadan/shop-kbeauty/issues/62) | Store Owner | Delete a product | Remove items that are no longer for sale |
| 44 | [#72](https://github.com/JoyZadan/shop-kbeauty/issues/72) | Store Owner | Have policy pages (privacy, terms & conditions, return & refund and shipping) on the site | Be assured that all the legalities of doing business online are taken care of |
| 45 | [#76](https://github.com/JoyZadan/shop-kbeauty/issues/76) | Store Owner | Receive a warning if I accidentally click the delete a product button | Avoid accidental deletion of a product |
| 46 | [#83](https://github.com/JoyZadan/shop-kbeauty/issues/83) | Store Owner | Add a brand to my store | Add new products even if the product's brand is not in the store yet |
| 47 | [#84](https://github.com/JoyZadan/shop-kbeauty/issues/84) | Store Owner | Edit/ Update a brand in my store | Make changes to a brand name, description, brand logo or choose to feature a brand |
| **DIGITAL MARKETING** |   |   |
| 48 | [#26](https://github.com/JoyZadan/shop-kbeauty/issues/26) | Store Owner | Have a social media presence | Create awareness of Shop K-Beauty products |
| **USER'S WISHLIST** |   |   |
| 49 | [#85](https://github.com/JoyZadan/shop-kbeauty/issues/85) | Shopper | Easily add a product to my wishlist | Save it for future purchase or reference |
| 50 | [#87](https://github.com/JoyZadan/shop-kbeauty/issues/87) | Shopper | Easily remove a product from my wishlist | Keep only the products I'm interested in | -->

## STRUCTURE PLANE
### **Interaction Design**
#### **User Flow Diagram**
![Catnip Cove User Flow Diagram: logged in superuser, logged in user, and anonymous donator]

### **Database Design**
<!-- When designing an efficient, useful database for Shop K-Beauty, we followed the following phases:
1. Requirements Analysis - identifying the purpose of the database
2. Organizing data into tables - determining the database structure
3. Normalizing to standardize the tables -->

Source: [Lucidcart Database Diagram/ Database Design]

<!-- How were these phases conducted and completed?
1. Requirements Analysis - identifying the purpose of the database
This first phase was completed after the following information were gathered/ determined:
* During the Discovery Phase (Please refer to Strategy Plane > Project Goals > User Research > Discovery Phase), test users were interviewed about how they normally shop (online) for skincare and hair &amp; body products in order to learn more about their buying process, the information they typically look for when buying said products and any other information they require to help them decide which product to purchase.
* Additional insights were also gathered by researching similar online shops to find out what information they typically include in their product detail page, the steps from browsing a product to buying the product, and what information they require a shopper to provide. Finally, their search, sorting and filtering functionalities were also perused for insights.
2. Organizing data into tables - determining the database structure
* The second phase took several iterations to complete. First, the database tables were created for each so-called real-world entities such as an individual (person), the things (products, product classification and data about the products) and also the places (personal information, address details, etc). The purchasing process itself was mapped to determine what data will be needed, generated and stored.

* These tables are the visual representation of the data that will be in the database and as the project development progressed, as and when required, we refined the tables by adding, amending, moving or deleting the data types in each table.

* Analysing the relationships between these tables was an important step to identify the cardinality (cardinality refers to the quantity of elements that interact between two related tables - source: [Lucidcart Database Diagram/ Database Design](https://www.lucidchart.com/pages/database-diagram/database-design)) to ensure that the data have been divided into tables efficiently. The relationships between entities were also determined whether they are:
    * one-to-one relationships
    * one-to-many relationships
    * many-to-many relationships

* In the case of many-to-many relationships, these were then further divided by creating another table to become one-to-many relationships.

3. Normalizing to standardize the tables
* As an ecommerce store, Shop K-Beauty's databases are good candidates for normalization as the users (Shop Owners, Superadmins and Shoppers) are concerned with creating, reading, updating and deleting (CRUD) records.
* As an example, the product tables can only have one value of say, product brand. There cannot be two brands for one product. -->

#### **Database ERD**
**Entity Relationship Diagram**<br/>
This ER diagram captures the relationships between real-world entities. The entities are the data points of objects such as persons, places and things and together with their attributes, compose their domain, ie, their individual table. The cardinality (relationships) between these entities are then mapped and identified (see **Database Design** above).

[ERD Cardinality]() - Source: [Lucid Chart](https://lucidchart.zendesk.com/hc/en-us/articles/207299756-Entity-Relationship-Diagrams)

Initial ERD: [ERD/DATABASE SCHEMA - V1]<br/>
Final ERD: ![ERD/ DATABASE SCHEMA - V3]

#### **Data Modelling**
As evidenced by the database design and the ERD discussed above, the data model type used for this project is the Relational Model. Further readings about Relational Model can be found [here](https://www.guru99.com/relational-data-model-dbms.html).

Each of the models below are used for the project and contain the fields and behaviours of the data being created and stored.
##### *User Model*
- The User model is a component of Django's Authentication system and contains information about the user.
- The User model contains the following fields: username, email, first_name, last_name, password, is_staff, is_active, is_superuser, date_joined, and last_login.

##### *UserProfile Model*
- The UserProfile model is an extension of the Django User model and has a one-to-one relationship with it.
- The UserProfile model contains the following fields: user, default_phone_number, default_postcode.
- The UserProfile model is included in the installed profiles application.

##### *Cats Model*
- The Cats model contains the following fields: .
- It is one of the models included in the installed Cats application.
- It is one of three original custom Django models created for the project.

##### *Category Model*
- The Category model contains the following fields: name, friendly_name and slug.
- It also contains Main_Category as a ForeignKey
- It is one of the models included in the installed products application.

##### *Subcategory Model*
- The Subcategory model contains the following fields: name, friendly_name and slug
- It also contains Category as a ForeignKey
- It is one of the models included in the installed products application.
- It is one of FIVE original custom Django models created for the project.

##### *Donation Model*
- The Donation model contains the following fields: and stripe_pid.
- It also contains UserProfile as a ForeignKey.
- It is one of the models included in the installed Donation application.


## **SKELETON PLANE**
### **Wireframes**
The wireframes were created using [Lucidchart](https://www.lucidchart.com/pages/templates/wireframe).

* Home Page
![Home Page Wireframe]()

## **SURFACE PLANE**
### **Typography**

<br/><br/>
![ FONT]

### **Colour Palette**


### **Imagery**

---

## **Defensive Programming**
<!-- To keep the site secure and protected against a brute force attack or attempts to access pages reserved solely based on user permission levels, defensive programming was at the forefront of the development.

* I implemented login_required functionality across relevant views and templates.
* On specific views.py files, I made sure to check if the user is authenticated and when required, the user's permission level.

Defensive programming is also implemented to handle bad user inputs or actions and their unintended consequences. One such example is the use of modals to confirm the intent of deleting a product or a review to avoid the unintended deletion of data.

**Update**: deleting a product when it is still in the shopping bag caused an unnecessary 404 error. This was fixed by amending the modal popup to warn the shop owner to first check that this is not the case prior to deleting the product. -->

**Defensive Programming at work:**
* Edit a brand: user is logged in but without the correct permission level
![Edit a brand -logged in user without the correct permission level](./documentation/features/edit-brand-logged-in-not-superadmin-user.gif)

* Incognito Mode - edit a brand - user is not logged in
![Incognito Mode - edit a brand - user is not logged in](./documentation/features/edit-brand-incognito-mode-user-not-logged-in.gif)

* Add a product - logged in user without the correct permission level
![Add a product - logged in user without the correct permission level](./documentation/features/add-product-logged-in-not-superadmin-user.gif)

* Modal
![Modal](./documentation/features/modal.png)
* updated modal warning
![Update: modal popup warning](./documentation/features/modal-updated.png)

## **Accessibility**
To ensure that the Shop K-Beauty site will be as usable by as many visitors and shoppers alike, I ensure that the site is accessible by:
* using Semantic HTML
* using descriptive alt attributes on images used on the site
* providing the order, role and accessible name (what is read by a screen reader) for all navigable elements that are used on the site
* providing ARIA attributes where they are needed
* ensuring that there is sufficient colour contrast throughout the site
* converting png images to next generation webp versions to achieve better compression and making the site usable for those onn low network speed

<!-- I tested the Shop K-Beauty's accessibility using Lighthouse and WAVE and fixed any errors highlighted, including amending the colour scheme used for the site. -->

<!-- ## **Extra Meta Tags for Specific Pages**
The extra meta tags on specific pages of the site allow for a tailored image and content when posting on social media pages. Using the content (page title, page description and target keywords) that came out of the **Integrating Content Strategy and SEO exercise (SCOPE PLANE)** plus images, the result is a more engaging social media posts that actually help deliver the intended message as opposed to a generic one.

Having these extra meta tags feature is particularly important for Shop K-Beauty as a business because the rise and continuing success of K-Beauty products as a whole becoming a global phenomenon are in large part driven by social media. Straits Research, in its report entitled, [K-Beauty Products Market Trend, Growth to 2022-2030](https://straitsresearch.com/report/k-beauty-products-market), the section on **Market Dynamics (Global K-Beauty Products Market Drivers)** discussed in detail that the *popularization of products are inspired by unique ingredients as well as digital marketing strategies.* The report added, *The West's journalists and social media influencers have also been interested in the K-Beauty boom. The K-Beauty businesses have been praised for using this as an inventive digital technique to get more popularity.*

**Extra meta tags and examples of how they work on [Shop K-Beauty's social media page (Facebook)](https://www.facebook.com/shopkbeauty.new):**
1. Products page shared on social media:
* ![Products page shared on social media](./documentation/features/products-page-facebook-post.png)

2. Product detail page shared on social media:
* ![Product detail post](./documentation/features/product-detail-page-facebook-post.png)

3. Brands page shared on social media:
* ![Brands page shared on social media](./documentation/features/brands-page-facebook-post.png)

4. Brand detail page shared on social media:
* ![Brand detail post](./documentation/features/brand-detail-page-facebook-post.png)

The meta tags are also in place to dynamically change what's displayed on the browser tabs, for example when the product detail page is opened, the name of the product comes up first followed by the site's title. This is particularly important as the slugs are not being utilised in place of product IDs.

* Product Name on the browser tab
    * ![Product name on the browser tab](./documentation/features/product-name-on-browser-tab.png)
* Brand Name on the browser tab
    * ![Brand name on the browser tab](./documentation/features/brand-name-on-browser-tab.png) -->

<!-- ## **Multi Brands**
As a reseller of K-Beauty products, Shop K-Beauty carries inventories from different brands, providing a convenient access to a wider range of *use at home* K-Beauty products. Shop K-Beauty's wide selection of K-Beauty products also enable customers to shop for skincare and hair &amp; body K-Beauty products with varied price range and discounts. These two key points help the Shop to achieve the project goals of solving two out of three problems discussed in the beginning of this document:

* Project Goals:
    * Problems we are trying to solve:
        * *Problem 1: Convenient access to effective K-Beauty products that can be used at home without the help of medical aesthetician*
        * *Problem 3: Expensive skincare and hair & body products*

See also **Strategy Plane: Project Goals** above.

As the shoppers are able to **Shop by Brand** via the Brands page, they are able to easily find the brands and products that they prefer.

Lastly, as some shoppers may be new to K-Beauty, trust about the K-Beauty concept becomes a more important factor that must be addressed. By offering a wide selection of brands to choose from and featuring a selection of these brands, Shop K-Beauty is able to provide a stronger user experience that also rivals what shoppers expect when browsing a brick and mortar retail shop that tend to carry multiple brands.

## **Brand Management - Authorized Personnel Only**
As a multi brand ecommerce shop specialising in K-Beauty, being able to manage the brands is a necessity.

Logged in Shop Owners are able to add a new brand or update an existing one at the click of a button directly at the store. At the top navigation, from the My Account area, one of the dropdown options is **Brand Management** that then takes the shop owners to the brand management page where they can easily add a new brand to the store.

![Link to Brand Management](./documentation/features/brand-management-button.png)

The brand management page provides the input fields for adding a new brand and also includes help texts underneath the required fields. These fields are:
* Brand name
* Friendly name
* Brand slug
* Brand description
* Select image button
* Is featured checkbox

Underneath the form are two buttons, one to cancel the action and redirects the shop owner to the brands page and the other button is add brand.

After a brand is successfully added, the shop owner will be redirected to the new brand's brand detail page.
* brand management: add a brand page
![brand management: add a brand](./documentation/features/brand-management-add-brand.png)

To edit a brand, the shop owners only need to go to the brand detail page where underneath the brand description is the edit brand button. Clicking this button will open the brand management page - edit brand where the form fields are already pre-populated with the available data about the brand such as name, friendly name, slug, description, image and is featured checkbox. A toast also shows an alert that the brand is being edited.
* edit brand button on the brand detail page (visible only to logged in Shop Owners)
![edit brand button](./documentation/features/edit-brand-button.png)
* brand management: edit a brand page
* ![brand management: edit a brand](./documentation/features/brand-management-edit-brand-page.png)

Deleting a brand requires the shop owners to log in to the Django administration page. This is because editing a brand will also delete all the products of that brand and requires more complexity that needs to be tackled in future development.

## **Product Management - Authorized Personnel Only**
Logged in Shop Owners are able to perform the full CRUD (create, read, update and delete) product management operations directly at the store.

To add a new product, at the top navigation, from the My Account area, one of the dropdown options is **Product Management**. This takes the shop owners to the product management page where they can easily add a new product to the store.

![Link to Product Management](./documentation/features/brand-management-button.png)

The product management page provides the input fields for adding a new product and also includes help texts underneath the required fields. These fields are:
* Main category title
* Category title
* Subcategory title
* Brand title
* Sku
* Product name
* Product slug
* Is featured checkbox
* Total quantity
* Total availability
* Product description
* How to use
* Product ingredients
* Has sizes
* Price
* Discount
* Original price
* Select image button

Underneath the form is a cancel button and an add product button. The cancel button redirects to the products page. If there is no error in adding the product, the add product button redirects to the newly added product detail page. On the other hand, if there is an error in adding the product, a help text will appear underneath the form field where the error occured.

* product management: add a product
![product management: add a product](./documentation/features/product-management-add-product.png)

* product management: add a product - error
![product management: add a product - error](./documentation/features/product-management-add-product-error.png)

To edit a product, the shop owners only need to go to the product detail page where underneath the product image is the edit product button. Clicking this button will open the product management page - edit product where the form fields are already pre-populated with the available data about the product (as above). A toast also shows an alert that the product is being edited.

* edit product button on the product detail page (visible only to logged in Shop Owners)
![edit product button](./documentation/features/product-management-edit-product-button.png)
* product management: edit a product
![product management: edit a product](./documentation/features/product-management-edit-product.png)

To delete a product, next to the edit a product button is the Delete Product button that when clicked opens a modal to confirm the intent of deleting a product to avoid the unintended deletion of data. (See also **Defensive Programming** above.) -->

<!-- ## **Product Reviews**
On the product detail page, product reviews (if available) are visible to all users by clicking the **see all reviews** button below the product image. Some reviews, if featured are displayed below the accordion. All the reviews has the same design and displays the same type of content:
* review title
* posted by: *username*
* date
* review content

To add a review, shoppers must be authenticated. After clicking the **add a review** button on the product detail page, a shopper is taken to the add a review page with the product information displayed on the right of the screen (desktop and tablet) or bottom of the screen (mobile). The product information includes the image, name, category, subcategory, price, original price and discount (if available) plus a shop now button that links back to the product detail page.

* see all reviews and add a review buttons
    * [reviews buttons](./documentation/user_stories_testing/user-stories-34-view-available-reviews-part1.png)
* all available reviews
    * [available reviews for specific product](./documentation/user_stories_testing/user-stories-34-view-available-reviews-part2.png)
* add a review
    * ![add a review form](./documentation/user_stories_testing/user-stories-36-review-form-and-product-info.png)

Store Owners are able to feature a product review using the Django admin backend by simply ticking the **Is featured** checkbox.
* [feature a review](./documentation/user_stories_testing/user-stories-38-featured-review.png)

Authenticated shop owners are currently able to edit the reviews directly at the store. The **edit** button is displayed underneath the review content.
* [edit review](./documentation/user_stories_testing/user-stories-39-edit-submitted-reviews.png)

A logged in store owner is able to also delete a review. To prevent unintended deletion, a modal pops up a warning that such action will delete the review forever if they continue. The option to cancel and delete buttons are also included in the modal.
* [delete review modal](./documentation/user_stories_testing/user-stories-40-delete-review-modal.png)

## **Related Products**
There are numerous advantages to having a related products section on an ecommerce store. According to [ShopFactory](https://www.shopfactory.com/contents/en-us/p1567_The-benefits-of-showing-related-items-to-buyers-in-your-ShopFactory-online-store.html), *Related and recommended products can help boost sales by making buyers aware of other products available to them or providing more information to help them with their purchasing decisions.*

Related Products are one of the many features implemented on Shop K-Beauty in order to:
1. Give more options to the customers andd improve the shopping experience for buyers since they don't have to search for relevant items. This also introduces products to shoppers they may not yet know about.
2. Meet user expectations since multi-national online stores as well as small and medium e-commerce shops already implement this system, shoppers expect to see a related product section.
3. Builds more trust. Related products are a great way for the budget conscious shoppers to find the product that they want at a price point that they need.

On the product detail page, below the featured reviews (if available) or below the accordion are four or less related products based on the product's subcategory. The related products are displayed randomly if there's more than four of them. Each related product card has the product name, category, subcategory, price, original price and discount (if they exist) and a shop now button.

* related products
    * ![related products](./documentation/user_stories_testing/user-story-13-related-products.png) -->

## **Site Features Common to All Pages**
Common to all pages of the Shop K-Beauty site are:

* **Favicon**
    The favicon is an effective visual reminder of the site's identity in the browser tabs and has been tested against the following browsers:
    1. Safari
    2. Google Chrome
    3. Microsoft Edge
    4. Firefox
    * Favicons
        * ![Favicons screenshot](./documentation/features/shop-kbeauty-favicons.png)

* **Navbar**
    The navbar has two main components, the top navigation and the main navigation. The first component is the top navigation (see below). It shows the site's logo, visitors can search for products using the search bar, sign up or login via the My Account icon and view the grand total of items in their bag. The second component is the main navigation that allows the visitors to browse for products, special offers, brands and K-Beauty tips. The navbar and all its components are fully responsive, as evidenced by the screenshots below.

    * **Top Navigation**:
        * logo (text-based logo)
        * search bar (visitors can search for products, brands and ingredients)
        * my account (login, register)
            * for logged in superadmin:
                * brand management
                * product management
                * my profile
                * logout
            * for logged in users (no superadmin permissions):
                * my profile
                * logout
        * wishlist (for logged in users)
        * bag

        Top Navigation screenshots<br/>
        1. Top Navigation - desktop
        * ![Top Navigation - desktop](./documentation/features/top-navigation-desktop.png)
        2. Top Navigation - mobile
        * ![Top Navivation - mobile](./documentation/features/top-navigation-mobile.png)
        3. Top Navigation - desktop - logged in superadmin user
        * ![Top Navigation - desktop - logged in superadmin user](./documentation/features/top-navigation-desktop-logged-in-superadmin.png)
        4. Top Navigation - tablet - logged in user
        * ![Top Navigation - tablet - logged in user](./documentation/features/top-navigation-tablet-logged-in-user.png)
        5. Top Navigation - mobile - logged in user: wishlist icon is displayed
        * ![Top Navigation - mobile - logged in user: wishlist icon is displayed](./documentation/features/top-navigation-mobile-wishlist-logged-in-user.png)

    <br/>

    * **Main Navigation**
        * all products dropdown
            * view products by brand, price, discount, category, subcategory, all products
        * skincare dropdown
            * view skincare product types by categories, subcategories and all skincare
        * hair &amp; body dropdown
            * view hair &amp; body product types by categories, subcategories and all hair &amp; body
        * special offers dropdown
            * view deal types by new arrivals, top deals, clearance and all special offers
        * brands
        * k-beauty tips

        Main Navigation screenshots<br/>
        1. Main Navigation - desktop
        * ![Main Navigation - desktop](./documentation/features/main-navigation-desktop.png)
        2. Main Navigation - tablet - before
        * ![Main Navigation - tablet - before](./documentation/features/main-navigation-tablet-before.png)
        3. Main Navigation - tablet - after
        * ![Main Navigation - tablet - after](./documentation/features/main-navigation-tablet-after.png)
        4. Main Navigation - mobile - before
        * ![Main Navigation - mobile - before](./documentation/features/main-navigation-mobile-before.png)
        5. Main Navigation - mobile - after
        * ![Main Navigation - mobile - after](./documentation/features/main-navigation-mobile-after.png)

* **Delivery Banner**
    The banner area is currently being used to flag the free delivery threshold.

    Delivery Banner screenshots
    1. mobile
    * ![mobile](./documentation/features/delivery-banner-mobile.png)
    2. tablet
    * ![tablet](./documentation/features/delivery-banner-tablet.png)

* **Footer**:
    * Shop K-Beauty fictitious address, email and phone number
    * About - brief blurb about the shop
    * Policies - links to privacy policy, terms and conditions, return and refund policy and shipping policy pages
    * Follow Us - Social Media Links (Facebook, Instagram, Pinterest and Twitter)
        * I created a mock business page only for Facebook. I wanted to create an example of how a well thought out SEO strategy + the extra meta tags on specific pages can work well together to provide a better user experience for visitors and shoppers as well as save the shop owners the time to have to tailor every social media post, especially when they want to promote or call attention to specific products, brands or special deals.
    * Payment Processing Statement
    * Copyright and Disclaimer

    Footer screenshots
    1. footer on mobile
    * [mobile](./documentation/features/footer-mobile.png)
    2. footer on tablet
    * [tablet](./documentation/features/footer-tablet.png)
    3. desktop
    * ![desktop](./documentation/features/footer-desktop.png)

## **Site Pages**
### **Home Page**
Shop K-Beauty's home page features the following:
* "Above the fold":
    * A background hero image showcasing some of the globally renowned K-Beauty brands.
    * An attention getting Call to Action text announcing the arrival of the latest collections and a "shop now" button that links to new arrivals
* "Below the fold":
    * Featured Products
    * Featured Brands
    * See All Brands Button

Home page screenshot
![Homepage - Laptop](./documentation/features/shop-k-beauty-homepage-laptop-large-1440x1207.webp)<br/>

### **Products Page**
The products page contains the following:
* Badges to display the category names or specific subcategory when visitors click any of the links on skincare, hair &amp; body and special offers (navlinks).
* The number of products available (left side of the screen on desktop and tablet and centre on mobile) plus a link to "View All Products" when a visitor clicks on any of the navigation links on All Products, Skincare, Hair &amp; Body and Special Offers. These navlinks act as filtering mechanism to dynamically change the number of available products.
* A sorting functionality (right side of the screen on desktop and tablet and centre on mobile) for the visitors to sort the products by:
    * Brand (A-Z, Z-A)
    * Price (low to high, high to low)
    * Discount (high to low, low to high)
    * Name (A-Z, Z-A)
    * Category (A-Z, Z-A)
    * Subcategory (A-Z, Z-A)
* The result of products being filtered can still be sorted further.
* Individual products cards displaying the product image, name, category, subcategory, current price, original price (crossed out), savings and a shop now call to action button that then links to a product detail page. The currency is set to GBP.
* The product card has a gentle transition on hover.

Products page screenshots
1. Products Page on mobile
* [mobile](./documentation/features/products-page-on-mobile.png)
2. Products Page on tablet
* [tablet](./documentation/features/products-page-on-tablet.png)
3. Products Page on desktop
* ![desktop](./documentation/features/products-page-on-desktop.png)
4. All Products sorted by discount (high-to-low)
* [all products sorted by discount](./documentation/features/all-products-sorted-by-discount-high-to-low.png)
5. All Products filtered by subcategory
* [products filtered by subcategory](./documentation/features/all-products-filtered-by-subcategory.png)
6. All Products filtered by category
* [products filtered by category](./documentation/features/all-products-filtered-by-category.png)
7. All Products filtered by multiple categories
* ![products filtered by multiple categories](./documentation/features/all-products-filtered-by-multiple-categories.png)

### **Product Detail Page**
The product detail page contains the following: <br/>
Centre of screen on mobile and left side of the screen on tablet and bigger screens:
* Product image
* Right below the product image are two CTA buttons:
    * See all reviews button (if a review exists)
    * Add review button

Centre of screen on mobile and right side of the screen on tablet and bigger screens:
* Product name
* Product brand - this links to the brand detail page
* Wishlist icon - right text of product brand that redirects to login page if user is not logged in, or adds the product to a user's wishlist
* Product category - this links to all products page, filtered by the product's category
* Product subcategory - this links to all products page, filtered by the product's subcategory
* Product price
* Crossed out original product price - if higher than the product price
* Saved amount from discount (if a discount exists)
* Quantity buttons to increment or decrement item quantity
* Two CTAs next to each other (tablets and above, otherwise one on top of the other) to either keep shopping or add product to bag
* An accordion that contains the product description, how to use and ingredients

Below all of the above are the following:
* Featured reviews, if they exist and a CTA to share experience of using the product, ie, add a review
* Four or less related products with a shop now call to action button on each product card.

Product detail page screenshot
![desktop](./documentation/features/product-detail-page.png)

### **Brands Page**
The brands page contains all available brands via individual brand cards that displays the brand logo. Each brand card links to the brand detail page.

Below then brand cards is a CTA button to view all products.

Brands page screenshot
1. Brands page on desktop
* ![desktop](./documentation/features/brands-page-desktop.png)
2. Brands page on tablet
* [tablet](./documentation/features/brands-page.png)
3. Brands page on mobile
* [mobile](./documentation/features/brands-page-mobile.png)

### **Brand Detail Page**
The brand detail page contains the following:
* the brand's logo
* the brand name
* the brand description
* list of available products from the brand - these products are displayed in individual product card that contains the product name, category, subcategory, price, original price and discount (if they exist) and a CTA to shop now
* a CTA to keep shopping that links to the products page

Brand detail page screenshot
1. Brand detail page on desktop
* ![desktop](./documentation/features/brand-detail-page.png)
2. Brand detail page on tablet
* [brand detail page - tablet](./documentation/features/brand-detail-page-tablet.png)
3. Brand detail page on mobile
* [brand detail page - mobile](./documentation/features/brand-detail-page-mobile.png)

### **Bag Page**
The bag page is fully responsive and contains the following:
* product info
    * product image
    * product name
    * product size, if available, otherwise N/A
    * product SKU
* product price
* quantity buttons to increment or decrement product quantity
* update button to update the product quantity currently in the bag (in case the shopper decide)
* remove button to remove the product from the bag
* bag total
* delivery cost
* grand total of products in the bag
* if the grand total is below the delivery threshold, a text in red will show the shopper how much they need to spend to get free delivery
* keep shopping CTA button which links to the products page
* secure checkout which opens the checkout page

The session is enabled so an anonymous shopper can continue browsing for other products and the items in the bag will stay in the bag as long as the site's connection to the browser does not get disconnected.

Should the shopper add a product that is already in the bag, the product quantity will increment and a toast message will appear to state that the item quantity has been updated to the total number of product items added in the bag.


### **Checkout Page**
The checkout page has two sections: the personal information and delivery form and the order summary. <br/> The personal information form includes the fields a shopper must complete for an order to be processed and has three main areas: the details, delivery and payment. The details area is for full name and email address; the delivery area has required fields (phone number, street address1, town or city and a dropdown to select the country) and the not required fields (street address2, county, state or locality and the postal code). An anonymous shopper can choose to create an account or login to save their delivery information. The payment area includes the input fields for the credit card number, the month and year or expiry and the Card Verification Code (CVC).

The order summary section of the checkout page contains the information on the items in the shopper's shopping bag. It displays the product image, name, size, quantity of item, the subtotal, the order total, the delivery cost and the grand total.

Below the payment area are two buttons: adjust bag button (which links back to the shopping bag page) and the complete order button. Underneath these two buttons is a reminder of how much the shopper's card will be charged with the grand total amount.

After clicking the complete order button, Stripe will process the payment.

Meanwhile, if a shopper is already logged in and has previously filled out their profile's default delivery information, these data will be used to pre-populate their checkout form.

Lastly, if there's an error in filling out the form, the form gives an error at the time of submission and through a help text provides feedback to the shopper where the error occured what needs to be corrected.

Errors in the payment area such as providing a card year that has expired are also handled by a help text.
A form is provided for filtering the orders by date for a better user experience.


Checkout page screenshot
1. Checkout page on desktop
* ![checkout page - desktop]

### **Checkout Success Page**
After a successful processing of an order, the shopper is redirected to the checkout success page where a receipt shows the order info, the order details, delivering to information and the billing info. A toast also informs the the shopper that the order has been successfully processed, the number number and that a confirmation email will be sent to the email address provided at checkout.

At the bottom of the page, a call to action button to checkout the latest deals allows the shopper to go the products page, filtered to display all products in the new arrivals, top deals and clearance categories.

![checkout success page]

### **Profile Page**
<!-- A logged in shopper's profile page contains:
* a greeting with their provided username
* a statement about what they will find in their profile page
* a wishlist button which will take them to their wishlist page
* the default delivery information that the shopper can update
* the update information button
* the shopper's order history which contains:
    * the order number receipts that each links back to the checkout success page where a receipt shows the order info, the order details, the delivering to information and the billing info. The toast this time shows an alert that this is a past confirmation for a particular order and that a confirmation email was sent on the order date.
    * the order dates
    * the order items' product name and the quantity
    * the order total

When a shopper updates their information, the profile page will reload, updates the data prepopulated on the form with the new data provided and a toast confirms that the profile updated successfully.

![profile page] -->


### **Sign Up Page**
A regular user can register and create an account with Shop K-Beauty from the Sign Up page. The Sign Up page can be accessed from the site's top navigation which has the My Account icon. This icon has two dropdown links, the first of which is the Sign Up. Clicking the Sign Up link opens the site's sign up page where they can then register to create an account. Alternatively, shoppers who do not yet have an account with the site can also create an account from a link at the checkout page.

* [sign up](./documentation/user_stories_testing/user-story-14-sign-up.png)
* [register an account](./documentation/user_stories_testing/user-story-14-register-for-account.png)
* [create an account link from checkout page](./documentation/user_stories_testing/user-story-14-checkout-create-an-account.png)

### **Verify Email Page**
After registering for an account, a shopper will receive an email with a link to confirm their new account. After clicking the email confirmation link, the site opens to the login page where the shopper's username or email and password are already pre-populated and a toast displaying that the email has been confirmed.

* [email-confirmation](./documentation/user_stories_testing/user-story-15-email-confirmation.png)
* [confirm email](./documentation/user_stories_testing/user-story-15-confirm-email.png)
* [login page after email is confirmed](./documentation/user_stories_testing/user-story-15-after-new-account-is-verified.png)

### **Log in Page**
The Log In page has a link to the sign up page right above the input fields for:
* username
* password

Below the input fields are:
* a remember me checkbox
* two buttons next to each other: link to the homepage and a login button
* underneath the two buttons is a forgot password link

* [log in page after email is confirmed](./documentation/user_stories_testing/user-story-15-after-new-account-is-verified.png)

### **Password Reset Page**
If registered users need to reset their password, from the accounts/login page, they have the option to click on the Forgot Password? link which takes them to the password reset page.

* [forgot password link](./documentation/user_stories_testing/user-story-17-forgot-password-link.png)
* ![password reset](./documentation/user_stories_testing/user-story-17-password-reset.png),

Resetting the password comes in several process (continues below):
* step 1 of 3) Enter the email address to receive a password reset email.

### **Change Password Page**
Resetting the password comes in several process (continues below):
* step 2 of 3) Open the password reset email that with the link that has the secure key added to take the user to the change password page.

Meanwhile, should a shopper enter an email that is not associated with any user account, the password reset page will display the error message.
* ![change password page](./documentation/user_stories_testing/user-story-17-change-password.png)

### **Password Changed Page**
Resetting the password comes in several process:
* step 3 of 3) Change the password. A successful password change is further confirmed by a toast message and the user can now login to their account with using their new password.

* password changed successfully
    * ![password changed successfully](./documentation/user_stories_testing/user-story-17-password-changed-success.png)
* error message if email is not in any user account
    * ![error message if email not in any user account](./documentation/user_stories_testing/user-story-17-password-reset-email-not-assigned-to-any-user-account.png)

### **Sign Out Page**
When an authenticated shopper selects the Logout link from the top navigation's My Accounts, they will be prompted to confirm if they are sure that they want to sign out.

The shopper can either choose to signout by selecting the corresponding button or cancel to be redirected back to the homepage without signing out. If they selected to sign out, a toast let's them know that they have successfully signed out.

* sign out page
    * ![sign out page](./documentation/features/sign-out-page.png)
* signed out toast
    * ![signed out toast](./documentation/features/signed-out-toast.png)


### **Error Pages**
The error pages on the site include custom pages for the following errors:
* 400
* 403
* 404
* 500

They all use the same background image and layout with only the content amended to reflect the error code and message to the user.

* ![404 error page]


---

# **Future Development, Iteration and Implementation**
| **FOR FUTURE IMPLEMENTATION** |   |
<!-- | --- | --- |
| 1 | Investigate further / fix the console log error for timed out event listener
| 2 | Add a product attribute model and properly set up the product prices depending on product size |
| 3 | Add an if else statement to delete product views to better handle situations encountered on solved bug # 17 |
| 4 | Add social media registration and login functionality |
| 5 | Add a stock inventory app so shop owners can keep track of product stock, display the product stock availability on product detail page and have a way to handle decrementing the product stock availability after every successful purchase. |
| 6 | Add an order management functionality to the store |
| 7 | Add email subscription and email marketing |
| 8 | Add a contact form |
| 9 | Add digital discount vouchers |
| 10 | Add a loyalty card |
| 11 | Add a digital gift card product |
| 12 | For better SEO, investigate further / fix the urls to use slug with dash and not id and not underscores |
| 13 | Add a maincategory, category and subcategory management functionality to the store |
| 14 | Add more content to K-Beauty tips page | -->

---
# **TECHNOLOGIES USED**
## **Languages Used**
* [HTML5](https://en.wikipedia.org/wiki/HTML5) was used for the content and structure of the site.
* [CSS3](https://en.wikipedia.org/wiki/CSS#CSS_3) was used for the styling of the site.
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript) was used for the interactivity of the site.
* [Python](https://www.python.org/) was used for the back end programming of the site.
## Frameworks Used
* [DJANGO - v3.2 ](https://docs.djangoproject.com/en/4.1/releases/3.2/) Django is a free and open-source, Python-based web  framework that follows the model–template–views architectural pattern.
* [Bootstrap4 - v4.6](https://getbootstrap.com/docs/4.6/getting-started/introduction/) was used as the frontend framework.
## Databases Used
* [DB.SQLITE3](https://docs.djangoproject.com/en/4.1/ref/databases/#sqlite-notes) was the database used for the project (development).
* [ElephantSQL](https://www.elephantsql.com/) ElephantSQL's Postgres as a Service was used to host the the database for the project (production).
## **Libraries and Packages Used**
* [django-allauth](https://django-allauth.readthedocs.io/en/latest/) is an integrated set of Django applications dealing with account authentication, registration, management, and third-party (social) account authentication.
* [JQuery - v3.5.1](https://jquery.com/) is a fast, small, and feature-rich JavaScript library.
* [Font Awesome Kit](https://fontawesome.com/v5/docs/web/setup/use-kit) is used for its icon toolkit.
* [django-countries, v7.2.1](https://pypi.org/project/django-countries/7.2.1/) was the Django application used to provide country choices for use with forms, and a country field for models.
* [django-crispy-forms, v1.14.0](https://pypi.org/project/django-crispy-forms/) was used to build programmatic reusable layouts out of form components.
* [gunicorn](https://gunicorn.org/) - a Python WSGI HTTP Server that allows us to run any Python application concurrently by running multiple processes within a single dyno
* [pillow](https://pypi.org/project/Pillow/) - a required Python imaging library used to enable handling of images.
* [psycopg2](https://pypi.org/project/psycopg2/) - a postgresql database adapter for python and used to connect with our postgres database
* [boto3==1.26.27](https://pypi.org/project/boto3/), [botocore==1.29.27] is an Amazon Web Services (AWS) software development kit (SDK) used to connect to the S3 bucket
* [pip](https://pip.pypa.io/en/stable/) is the package installer for Python, allowing us to install the packages we need for this site.
* [django storages](https://django-storages.readthedocs.io/en/latest/) - collection of custom storage backends for Django
* [coverage==7.0.4](https://coverage.readthedocs.io/en/7.1.0/) used after automated testings were written to find out the percentage of statements that I was able to cover and those that I missed for every installed application

## **Programmes and Applications Used**
* [Visual Site Maps](https://visualsitemaps.com/) was used to autogenerate Shop K-Beauty's visualized site map.
* [Lucid Chart](https://www.lucidchart.com/pages/) was used to draw and build the Entity Relationship Diagram. It was also used to draw the User Flow Diagram.
* [favicon.io](https://favicon.io/) used to create the site's favicon
* [Git](https://git-scm.com/) used for version control and saving work in the repository, using the GitPod extension in Google Chrome to commit to GitHub.
* [GitHub](https://github.com/) is the project's git repository
* [GitHub Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects) used to track and integrate issues for Agile Development
* [Chrome DevTools](https://www.google.com/intl/en_uk/chrome/) - used for debugging, validation (Lighthouse) and taking fullscreen screenshots of the site

## **Payment Processing Platform Used**
* [Stripe](https://stripe.com/gb) was used to test and implement the payment processing for the site.

Stripe how to test cards interactively:
| **CARD NUMBER** | **MM &amp; YY**  | **CVC** | **SIMULATED PAYMENT RESULT** |
| --- | --- | --- | --- |
| 4242 4242 4242 4242 | use any valid future month and year | use any three digit CVC | successful payment |
| 4000 0000 0000 0002 | use any valid future month and year | use any three digit CVC | generic decline |

## **Cloud Application Platforms Used**
* [Heroku](https://devcenter.heroku.com/) was used for hosting and deployment of the live site. Throughout, we have ensured the version being deployed to Heroku matches the development version by checking features and screen layouts on both versions.

## **Cloud Storage Services Used**
* [AWS S3](https://aws.amazon.com/) was used to store the images and static files.
---

# **TESTING**
Please refer to [TESTING.md](./TESTING.md) file for:
* Automated Testing and Validation Results
* Manual Testing and Results

<br/>

---
# **BUGS, ISSUES AND SOLUTIONS**
Please also refer to [TESTING.md](./TESTING.md) file for:
* Solutions to bugs found during testing and development phase
* Known bugs
<br/>

---
# **DEPLOYMENT**
Please refer to [DEPLOYMENT.md](./DEPLOYMENT.md) file for:
* Creating the database to be used in production
    * Instructions to common question: *"What if you didn't use fixtures in your project?"*
* Deploying to Heroku
* Setting up AmazonS3 for hosting our static and media files
---

# **CREDITS**
## **Code**
* Credit to [Code Institute's](https://codeinstitute.net/) Boutique Ado walkthrough, from which this project got its start.
*
* 
* 
* Credit to [Adam Johnson](https://adamj.eu/tech/2022/10/06/how-to-safely-pass-data-to-javascript-in-a-django-template/) on How to Safely Pass Data to JavaScript in a Django Template.
* Credit to [BugBytes](https://www.youtube.com/watch?v=h39eMGWmEV4) for his video based on Adam Johnson's post.
* 
* Credit to [Masa Kudamatsu at DEV.to](https://dev.to/masakudamatsu/loading-google-fonts-and-any-other-web-fonts-as-fast-as-possible-in-early-2021-4f5o) for his very helpful article, **Loading Google Fonts and any other web fonts as fast as possible in early 2021** which helped me increase the Lighthouse performance score (mobile) from 67% to 73%.
* 
* 
* Credit to [Ordinary Coders](https://ordinarycoders.com/blog/article/how-to-add-django-meta-tags) on guidance on *How to add meta tags to a Django HTML template*
* Credit to [CSS Tricks's The Essential Meta Tags for Social Media](https://css-tricks.com/essential-meta-tags-social-media/)
* 

## **Content**
The images, descriptions, brand logos and description and other information were sourced from:
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 



## **Media**
* All images were either created with AI or from pexels.com

## **Other Resources**
<!-- These other resources were used for research and/or for finding solutions when I got stuck.
1. [Stack Overflow](https://stackoverflow.com/)
2. [Very Academy](https://www.youtube.com/playlist?list=PLOLrQ9Pn6cay_cQkyg-WYYiJ_EKU8KWKh)
3. [Codemy YouTube](https://www.youtube.com/watch?v=HHx3tTQWUx0&list=PLCC34OHNcOtqW9BJmgQPPzUpJ8hl49AGy)
4. [CodingEx YouTube](https://www.youtube.com/watch?v=3cTVjPdP8ps&list=PLTV1jAY3nKHPPi74LSSsqiqG1H7pSlSj5)
5. [CodePiep YouTube](https://www.youtube.com/watch?v=AU9kjY2iZp0)
6. [The Open Graph Protocol](https://ogp.me/)
6. [Makneta Coding Journal](https://makneta.herokuapp.com/post/how-to-add-unique-meta-tags-in-django/) -->
---

# **ACKNOWLEDGEMENTS**


# *Copyrights*
 (An e-commerce Full Stack Developer Project)