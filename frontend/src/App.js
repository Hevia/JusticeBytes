import React, { useState }  from 'react';
import './App.css';
import { BaseProvider, LightTheme} from 'baseui';
import {Provider as StyletronProvider} from 'styletron-react';
import {Client as Styletron} from 'styletron-engine-atomic';
import SearchBar from './SearchBar';
import SearchResults from './SearchResults';

const engine = new Styletron();
const AppContext = React.createContext({});

function App() {
  const [searchResults, setSearchResults] = useState([{"url": "testing", "title": "none"}, {"url": "testing", "title": "none"}]);
  const [resultsFound, setResultsFound] = useState(false);
  const store = {
    searchResults: {get: searchResults, set: setSearchResults},
    resultsFound: {get: resultsFound, set: setResultsFound}
  }
  

  return (
    <StyletronProvider value={engine}>
      <BaseProvider theme={LightTheme}>
        <AppContext.Provider value={store}>
        {resultsFound ? <SearchResults stateContext={store}></SearchResults> : <SearchBar stateContext={store}></SearchBar>}
        </AppContext.Provider>
      </BaseProvider>
    </StyletronProvider>
  );
}

export default App;
