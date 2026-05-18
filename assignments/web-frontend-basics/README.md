# 📘 Assignment: Your First Webpage

## 🎯 Objective

Build a personal profile webpage using HTML for structure, CSS for styling, and JavaScript for a simple interactive element. You will learn how the three core technologies of the web work together.

## 📝 Tasks

### 🛠️ Build Your HTML Profile Page

#### Description
Create an HTML page that displays your personal profile. Use proper HTML document structure and a variety of HTML elements to present information about yourself.

#### Requirements
Completed program should:

- Include a valid HTML5 document structure (`<!DOCTYPE html>`, `<html>`, `<head>`, `<body>`)
- Display your name in an `<h1>` heading
- Include a short "About Me" paragraph using a `<p>` tag
- List at least three hobbies or interests using an unordered list (`<ul>` and `<li>`)
- Include a `<title>` in the `<head>` that shows your name

Example structure:
```html
<!DOCTYPE html>
<html>
  <head>
    <title>Alex's Profile</title>
  </head>
  <body>
    <h1>Hi, I'm Alex!</h1>
    <p>I love coding and solving puzzles.</p>
    <ul>
      <li>Chess</li>
      <li>Hiking</li>
      <li>Photography</li>
    </ul>
  </body>
</html>
```


### 🛠️ Style Your Page with CSS

#### Description
Add a `<style>` block inside your `<head>` to make your profile page look great. Experiment with colors, fonts, and spacing.

#### Requirements
Completed program should:

- Change the background color of the page
- Style the `<h1>` heading with a different font color and size
- Add padding or margin to the `<body>` so content isn't stuck to the edge
- Change the list style or color of the `<li>` items


### 🛠️ Add a JavaScript Interaction

#### Description
Add a button to your page that does something when clicked, using JavaScript inside a `<script>` tag.

#### Requirements
Completed program should:

- Include a `<button>` element with a descriptive label (e.g., "Say Hello!")
- Use a JavaScript `onclick` handler or `addEventListener` to respond to the click
- Change something visible on the page when the button is clicked (e.g., update a `<p>` tag's text, change a color, or show a hidden message)

Example:
```html
<button onclick="greet()">Say Hello!</button>
<p id="message"></p>

<script>
  function greet() {
    document.getElementById("message").textContent = "Hello, World!";
  }
</script>
```
