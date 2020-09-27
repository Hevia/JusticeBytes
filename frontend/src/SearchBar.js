import React from "react";
import "./App.css";
import { DarkTheme, useStyletron } from "baseui";
import { Input, SIZE } from "baseui/input";
import { Button } from "baseui/button";
import axios from "axios";

function SearchBar(props) {
  const [value, setValue] = React.useState("");
  const [css, theme] = useStyletron();
  console.log(css);

  const handleKeyPress = (event) => {
    if (value !== "" && event.key === "Enter") {
      event.preventDefault();
      makeSearchRequest(value);
    }
  };

  async function makeSearchRequest(user_input) {
    const response = await axios.post(
      "https://justicebytes-backend.azurewebsites.net/search",
      { search_query: user_input },
      { headers: { "Content-Type": "application/json" } }
    );
    Promise.all(response).then(() => {
      console.log(response.data)
      props.stateContext.searchResults.set(response.data.search_query);
      props.stateContext.resultsFound.set(true);
    });
  }

  return (
    <div>
      <svg className="homepage-logo"></svg>
      <div className="homepage-body">
        <div className="homepage-search-bar">
          <Input
            theme={DarkTheme}
            className="search-bar"
            value={value}
            onChange={(e) => setValue(e.target.value)}
            size={SIZE.default}
            placeholder="What would you like to know?"
            clearOnEscape
            onKeyDown={handleKeyPress}
            overrides={{
              Root: {
                style: {
                  width: "100%",
                  marginRight: theme.sizing.scale300,
                },
              },
            }}
          />
          <Button
            className="search-button"
            onClick={async () => await makeSearchRequest(value)}
          >
            Search
          </Button>
        </div>
      </div>
    </div>
  );
}

export default SearchBar;
