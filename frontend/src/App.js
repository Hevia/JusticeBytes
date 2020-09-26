import React from 'react';
import './App.css';
import { BaseProvider, DarkTheme, LightTheme, useStyletron} from 'baseui';
import { Input, SIZE  } from "baseui/input";
import {Button} from 'baseui/button';
import {Provider as StyletronProvider} from 'styletron-react';
import {Client as Styletron} from 'styletron-engine-atomic';
import axios from 'axios';

const engine = new Styletron();



function App() {
  const [value, setValue] = React.useState("What would you like to know?");
  const [_, theme] = useStyletron();

   async function makeSearchRequest(user_input) {
    const response = await axios.post(
      'http://127.0.0.1:8000/testJSON',
      { search_query: user_input },
      { headers: { 'Content-Type': 'application/json' } }
    )
    console.log(response.data)
  }


  return (
    <StyletronProvider value={engine}>
    <BaseProvider theme={LightTheme}>
    <div className="homepage-body">
      <div className="homepage-search-bar">
        <Input
        theme={DarkTheme}
        className="search-bar"
        value={value}
        onChange={e => setValue(e.target.value)}
        size={SIZE.default}
        placeholder=""
        clearOnEscape
        overrides={{
          Root: {
            style: {
              width: '100%',
              marginRight: theme.sizing.scale300,
            },
          },
        }}
      />
      <Button
        onClick={async() => await makeSearchRequest(value)}
      >Search</Button>
      </div>
    </div>
    </BaseProvider>
    </StyletronProvider>
  );
}

export default App;
