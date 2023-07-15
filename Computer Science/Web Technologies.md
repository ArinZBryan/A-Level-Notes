## Server-side vs Client-side
When we use the internet, there is an interaction between the two parties, the webserver and the client.

### Client-side
Any processing done on the client device must first be sent back to the server for it to appear in other's webpages. Generally, code run on client side is in javascript or webassembly. 

The advantages of this is that it can reduce web traffic (only if significant computation is done on the client, which is inadvisable) and that there is a generally snappier response for the suer, and that the server has less processing to do, so it can serve more clients.

### Server-side
Unlike client-side processing, server-side processing is far more flexible in what language it is run on. Some common languages are javascript, C#, ruby or python.

The advantages for server-side computation is that is far more secure, as any data sent to the client can be assumed compromised.

Generally, on the web, server-side rendering is used to increase the speed of the client by removing some client-side rendering, as well as the extra speed gained by querying the database from here, as they are likely running on the same machine as opposed to sending requests back and forth with the client.


## The process of searching for a term
When we enter a search term into a search engine, the whole of the internet is not being searched. When the search terms are sent to the search engine, it returns a cached list of pages (in this case called an index) that it has found using webcrawlers. 

These webcrawlers put together these lists of pages using the keywords and links in a page to determine what it is about, as well as using the number of links to a page to determine how '*good*' the page is. Of course, to remain dynamic and recent, the webcrawlers must return to pages many times, so that any new content is caught and can be added to the index. This process is called the '*pagerank*' algorithm.

Only once the user has selected a link from the index, is that page loaded.

### Search Engine Optimisation (SEO)
The pagerank algorithm:   
$R_{ank}(P_{A}) = (1-d) + d(\sum{\frac{R_{ank}(T_i)}{C_n}})$

where:  
$d$ = damping factor (based on percieved usage of site)  
$T_i$ = a site citing page A  
$C_n$ = the number of sites that site A cites.

## Rendering and Formatting a page
Web pages are made using a combination of HTML (Hyper-Text Markup Language), CSS (Cascading Style Sheets) and JS (Javascript) / WASM (WebAssembly).

It is important to note that the content of the page is determined by the HTML, and the look of the page is determined by the CSS. The JS/WASM components of the website control the function of the website, but can also be used to alter the function and style of a website in real-time depending on user input.

### HTML
HTML is a markup language, much like XML, that is based on a system of tags, such as 
```html
<div></div> <!--This is a general purpose division-->
<p></p>		<!--This is a paragraph-->
<a></a>		<!--This is a link-->
<h1></h1>	<!--This is a header of maximum size-->
<ol></ol>	<!--This is an ordered list-->
<ul></ul>	<!--This is an unorderd list-->
<li></li>	<!--This is an element of a list-->
```
Each tag may have various properties, such as a `src`, `href`, `class`, `id` or `name`, and must be closed using a closing tag.  
The HTML for a page defines the DOM (Document-Object-Model), a tree structure that defines the content and structure of the page.

### CSS
CSS is a styling language that operates on the HTML elements, giving them styles beyond the default.  
CSS generally works based on the `class` or `id` specified in the HTML (note that ids are for one element only).
```css
.classname {
	color: red;
	background-color: #ffa784;
	position: absolute;
	left: 30px;
	display: grid;
}

#id {
	color: blue;
	background-color: rgb(100%, 20%, 30%);
	position: relative;
	right: 20em;
	display: flex;
}
```

In CSS, there are many different units, from percentage based units, to pixels and units based on font size and zoom levels.  
The above code shows some example properties for HTML elements selected based on their class name and their id.  

### JavaScript
JavaScript (JS) is an interpreted scripting language that is run in the browser. It has the ability to edit the DOM's HTML and CSS directly and is an incredibly powerful programming language. It is also possible to run JavaScript code on the server, using a runtime such as NodeJS.

```js

let elem = Document.getElementById("classname");
elem.innerHTML = "This is the text in the element!";
alert("This will pop up a message on screen");
```

There are many more things that JavaScript can do, but this is one of the most important methods when working with HTML.

### WebAssembly
WebAssembly (WASM) is an intermediary JIT-Compiled language, that can be targeted by compilers such as LLVM and GCC. This allows for the running of other languages code in the browser, at near the speed of JavaScript. It should be known that calls to the browser do still have to pass through JavaScript to run though.

### Forms
Forms are a HTML element that can be used to take user input. An example form is shown below:
```html
<!DOCTYPE html>
<html>
  <head>
    <script>
    // Define a function which will be called when the button is clicked
    function greeting(){
      // Retrieve the value of the 'firstname' text box
      alert("Hello " + document.getElementById("firstname").value);
      }
    </script>
   </head>
<body>
  <form>
    <p>What is your name?</p> 
     <input type="text" id="firstname">
     <input type="submit" onclick="greeting()">
  </form>
</body>
</html>
```