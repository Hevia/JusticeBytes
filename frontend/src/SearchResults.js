import * as React from "react";
import './App.css';
import {
  Card,
  StyledBody,
  StyledAction
} from "baseui/card";
import { Button } from "baseui/button";

function SearchResults(props) {
  return (
  <div>
    <ul>
        {
            props.stateContext.searchResults.get.map(searchResult => (
                <Card className="search-result-card">
                    <StyledAction>
                    <Button
                    overrides={{
                        BaseButton: { style: { width: "50%" } }
                    }}
                    href={searchResult.url}
                    >
                    {searchResult.title}
                    </Button>
                </StyledAction>
                </Card>
            ))
        }
    </ul>
</div>
  );
}

export default SearchResults;
