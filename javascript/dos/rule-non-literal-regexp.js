// License: MIT (c) GitLab Inc.
const RE2 = require("re2");

module.exports = function (app) {

    const longStr = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa";
    const optionalFlags = undefined;

    // http://localhost:3000/dos/regex_injection_dos/match/1
    app.post('/dos/regex_injection_dos/match/1', (req, res) => {
        // ruleid: javascript_dos_rule-non-literal-regexp
        const arr =  longStr.match(req.body.regex)
        res.send("Check server console")
    })

    // http://localhost:3000/dos/regex_injection_dos/match/safe/1
    app.post('/dos/regex_injection_dos/match/safe/1', (req, res) => {
        // ok: javascript_dos_rule-non-literal-regexp
        const arr =  longStr.match(/a/)
        res.send("Check server console")
    })

    // http://localhost:3000/dos/regex_injection_dos/search/1
    app.post('/dos/regex_injection_dos/search/1', (req, res) => {
        // ruleid: javascript_dos_rule-non-literal-regexp
        const arr =  longStr.search(req.body.regex)
        res.send("Check server console")
    })

    // http://localhost:3000/dos/regex_injection_dos/search/safe/1
    app.get('/dos/regex_injection_dos/search/safe/1', (req, res) => {
        // ok: javascript_dos_rule-non-literal-regexp
        const arr =  longStr.search(/a/)
        res.send("Check server console")
    })

    // http://localhost:3000/dos/regex_injection_dos/re2/safe/1
    app.post('/dos/regex_injection_dos/re2/safe/1', (req, res) => {
        // ok: javascript_dos_rule-non-literal-regexp
        var re = new RE2(req.body.regex)
        re.exec(longStr)
        res.send("Check server console")
    })

    function test_positives_constructor(someVar, obj) {
      // ruleid: javascript_dos_rule-non-literal-regexp
      nonLiteral1 = new RegExp("double-quoted string" + someVar, optionalFlags)
      // ruleid: javascript_dos_rule-non-literal-regexp
      nonLiteral2 = new RegExp('single-quoted string' + someVar)
      // ruleid: javascript_dos_rule-non-literal-regexp
      nonLiteral3 = new RegExp('single-quoted string' + someVar, optionalFlags)
      // ruleid: javascript_dos_rule-non-literal-regexp
      nonLiteral4 = new RegExp(`template string ${someVar}`)
      // ruleid: javascript_dos_rule-non-literal-regexp
      nonLiteral5 = new RegExp(`template string ${someVar}`, optionalFlags)
      // ruleid: javascript_dos_rule-non-literal-regexp
      nonLiteral6 = new RegExp(someVar + "double-quoted string")
      // ruleid: javascript_dos_rule-non-literal-regexp
      nonLiteral7 = new RegExp(someVar + "double-quoted string", optionalFlags)
      // ruleid: javascript_dos_rule-non-literal-regexp
      nonLiteral8 = new RegExp(someVar + 'single-quoted string')
      // ruleid: javascript_dos_rule-non-literal-regexp
      nonLiteral9 = new RegExp(someVar + 'single-quoted string', optionalFlags)
      // ruleid: javascript_dos_rule-non-literal-regexp
      nonLiteral10 = new RegExp(someVar)
      // ruleid: javascript_dos_rule-non-literal-regexp
      nonLiteral11 = new RegExp(someVar, optionalFlags)
    }
    
    function test_positives_function(someVar, obj) {
      // ruleid: javascript_dos_rule-non-literal-regexp
      nonLiteral1 = RegExp("double-quoted string" + someVar, optionalFlags)
      // ruleid: javascript_dos_rule-non-literal-regexp
      nonLiteral2 = RegExp('single-quoted string' + someVar)
      // ruleid: javascript_dos_rule-non-literal-regexp
      nonLiteral3 = RegExp('single-quoted string' + someVar, optionalFlags)
      // ruleid: javascript_dos_rule-non-literal-regexp
      nonLiteral4 = RegExp(`template string ${someVar}`)
      // ruleid: javascript_dos_rule-non-literal-regexp
      nonLiteral5 = RegExp(`template string ${someVar}`, optionalFlags)
      // ruleid: javascript_dos_rule-non-literal-regexp
      nonLiteral6 = RegExp(someVar + "double-quoted string")
      // ruleid: javascript_dos_rule-non-literal-regexp
      nonLiteral7 = RegExp(someVar + "double-quoted string", optionalFlags)
      // ruleid: javascript_dos_rule-non-literal-regexp
      nonLiteral8 = RegExp(someVar + 'single-quoted string')
      // ruleid: javascript_dos_rule-non-literal-regexp
      nonLiteral9 = RegExp(someVar + 'single-quoted string', optionalFlags)
      // ruleid: javascript_dos_rule-non-literal-regexp
      nonLiteral10 = RegExp(someVar)
      // ruleid: javascript_dos_rule-non-literal-regexp
      nonLiteral11 = RegExp(someVar, optionalFlags)
    }
    
    function test_negatives_constructor() {
      // ok: javascript_dos_rule-non-literal-regexp
      literal1 = new RegExp('boom')
      // ok: javascript_dos_rule-non-literal-regexp
      literal2 = new RegExp("boom")
      // ok: javascript_dos_rule-non-literal-regexp
      literal3 = new RegExp(/pow!/)
    
      // ok: javascript_dos_rule-non-literal-regexp
      literalWithFlags1 = new RegExp('pew', optionalFlags)
      // ok: javascript_dos_rule-non-literal-regexp
      literalWithFlags2 = new RegExp("pew", optionalFlags)
      // ok: javascript_dos_rule-non-literal-regexp
      literalWithFlags3 = new RegExp(/pew!/, optionalFlags)
    }
    
    function test_negatives_function() {
      // ok: javascript_dos_rule-non-literal-regexp
      literal1 = RegExp('boom')
      // ok: javascript_dos_rule-non-literal-regexp
      literal2 = RegExp("boom")
      // ok: javascript_dos_rule-non-literal-regexp
      literal3 = RegExp(/pow!/)
    
      // ok: javascript_dos_rule-non-literal-regexp
      literalWithFlags1 = RegExp('pew', optionalFlags)
      // ok: javascript_dos_rule-non-literal-regexp
      literalWithFlags2 = RegExp("pew", optionalFlags)
      // ok: javascript_dos_rule-non-literal-regexp
      literalWithFlags3 = RegExp(/pew!/, optionalFlags)
    }
    
    function test_negatives_function_var() {
      var text = 'boom';
      // ok: javascript_dos_rule-non-literal-regexp
      literal1 = RegExp(text)
      // ok: javascript_dos_rule-non-literal-regexp
      literal2 = RegExp(text + "sd")
    
      var text = 'boom';
      // ok: javascript_dos_rule-non-literal-regexp
      literalWithFlags1 = new RegExp(text, optionalFlags)
      // ok: javascript_dos_rule-non-literal-regexp
      literalWithFlags2 = new RegExp(text + "sd", optionalFlags)
    }    
}