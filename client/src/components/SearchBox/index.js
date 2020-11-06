import * as React from "react";
import { Input } from "@rebass/forms";
import { Box } from "rebass";

const SearchBox = ({ query, setQuery, setLimit }) => {
  return (
    <Box>
      <Input
        id="search"
        name="search"
        type="text"
        placeholder="Enter a search term"
        value={query}
        onChange={(event) => {
          setQuery(event.target.value);
          setLimit(3);
        }}
      />
    </Box>
  );
};

export default SearchBox;
