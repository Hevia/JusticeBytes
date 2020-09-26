import React from 'react';

function SearchResults(props) {
  return (
  <div>{console.log(props.stateContext.resultsFound)}</div>
  );
}

export default SearchResults;
