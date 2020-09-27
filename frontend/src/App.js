import React, { useState } from "react";
import "./App.css";
import { BaseProvider, LightTheme } from "baseui";
import { Provider as StyletronProvider } from "styletron-react";
import { Client as Styletron } from "styletron-engine-atomic";
import Footer from "./Footer";
import SearchBar from "./SearchBar";
import SearchResults from "./SearchResults";

const engine = new Styletron();
const AppContext = React.createContext({});
const GITHUB_URL = "https://github.com/Hevia/JusticeBytes";

function App() {
  const [searchResults, setSearchResults] = useState([
    { url: "https://www.google.com/", title: "Google" },
    { url: "https://www.google.com/", title: "Google2" },
  ]);
  const [resultsFound, setResultsFound] = useState(false);
  const store = {
    searchResults: { get: searchResults, set: setSearchResults },
    resultsFound: { get: resultsFound, set: setResultsFound },
  };

  return (
    <StyletronProvider value={engine}>
      <BaseProvider theme={LightTheme}>
        <AppContext.Provider value={store}>
          {resultsFound ? (
            <SearchResults stateContext={store}></SearchResults>
          ) : (
            <SearchBar stateContext={store}></SearchBar>
          )}
        </AppContext.Provider>
      </BaseProvider>
      <Footer url={GITHUB_URL} />
    </StyletronProvider>
  );
}

export default App;
