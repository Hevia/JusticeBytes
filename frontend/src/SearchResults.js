import * as React from "react";
import './App.css';
import {
  Card,
  StyledAction
} from "baseui/card";
import { Button } from "baseui/button";

function SearchResults(props) {
  return (
  <div>
  <a href="/"><svg className="search-results-logo"></svg></a>
  <div className="search-result-box">
    <ul>
        {
            props.stateContext.searchResults.get.map(searchResult => (
                <Card className="search-result-card">
                    <StyledAction>
                    <a href={searchResult.url}>
                        <Button
                        className="search-result-button"
                        overrides={{
                            BaseButton: { style: { width: "100%" } }
                        }}>
                    {searchResult.title}
                    </Button>
                    </a>
                </StyledAction>
                </Card>
            ))
        }
    </ul>
    </div>
</div>
  );
}

export default SearchResults;
