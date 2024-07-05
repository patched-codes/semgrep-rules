// License: MIT (c) GitLab Inc.

const App = () => {
  const data = 'lorem <b>ipsum</b>';

  // ruleid:javascript_react_rule-dangerouslysetinnerhtml
  return (
    <div
      dangerouslySetInnerHTML={{__html: data}}
    />
  );
}

const App2 = () => {
  const data = 'lorem <b>ipsum</b>';

  // ok:javascript_react_rule-dangerouslysetinnerhtml
  return (
    <div>
      {data}
    </div>
  );
}

export default App;
