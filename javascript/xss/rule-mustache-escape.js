// License: MIT (c) JS Foundation and other contributors, https://js.foundation

module.exports = function (app) {
  const Mustache = require('mustache');

  const view = {
      data1: "<script>alert('Test alert!');</script>",
      data2: "<script>alert('Test-2 alert!');</script>",
      data3: "<script>alert('Test-3 alert!');</script>",
      data4: "<script>alert('Test-4 alert!');</script>",
      data5: "<b>GitHub</b>"
  };

  // ok:javascript_xss_rule-mustache-escape
  const output1 = Mustache.render("{{data1}}", view);
  // ruleid:javascript_xss_rule-mustache-escape
  const output2 = Mustache.render("{{{data2}}}", view);
  // ruleid:javascript_xss_rule-mustache-escape
  const output3 = Mustache.render("{{&data3}}", view);
  // ok:javascript_xss_rule-mustache-escape
  const output5 = Mustache.render("{{data5}}", view);
  // ruleid:javascript_xss_rule-mustache-escape
  const output6 = Mustache.render("{{{data5}}}", view);
  // ruleid:javascript_xss_rule-mustache-escape
  const output7 = Mustache.render("{{&data5}}", view);

  let htmlResponse = ` 
      <html> 
          <body>
              <h1>JavaScript Mustache Escape</h1>

              <h3>Test 1 - Variables are HTML-escaped by default, therefore script is not executed.</h3>
              <div>Template - {{data1}}</div> 
              <div>Data - `+output1+`</div>
              <div>Output - `+output1+`</div><br>
              <div>Template - {{data5}}</div>
              <div>Data - `+output5+`</div>
              <div>Output - `+output5+`</div><br>

              <h3>Test 2 - Using the triple mustache to render unescaped HTML.</h3>
              <div>Template - {{{data2}}}</div>
              <div>Data - `+output1+`</div>
              <div>Output - `+output2+`output is executed and displayed as alert(Test-2).</div><br>
              <div>Template - {{{data5}}}</div>
              <div>Data - `+output5+`</div>
              <div>Output - `+output6+`</div><br>

              <h3>Test 3 - Using the "&" to render unescaped HTML.</h3>
              <div>Template - {{&data3}}</div>
              <div>Data - `+output1+`</div>
              <div>Output - `+output3+`output is executed and displayed as alert(Test-3).</div><br>
              <div>Template - {{&data5}}</div>
              <div>Data - `+output5+`</div>
              <div>Output - `+output7+`</div><br>`;

  // ruleid:javascript_xss_rule-mustache-escape
  Mustache.escape = function(text) { return text; };
  // ok:javascript_xss_rule-mustache-escape 
  const output4 = Mustache.render("{{data4}}", view);
  // ok:javascript_xss_rule-mustache-escape
  const output8 = Mustache.render("{{data5}}", view);

  htmlResponse += `
              <h3>Test 4 - Disabled all escaping using "function(text) {return text;}"</h3>
              <div>Template - {{data4}}</div>
              <div>Data - `+output1+`</div>
              <div>Output - `+output4+`output is executed and displayed as alert(Test-4).</div><br>
              <div>Template - {{data5}}</div>
              <div>Data - `+output5+`</div>
              <div>Output - `+output8+`</div><br>

          </body>
      </html>`;

  app.get("/mustache-escape", async (req, res) => {
    res.send(htmlResponse);
  });
};
