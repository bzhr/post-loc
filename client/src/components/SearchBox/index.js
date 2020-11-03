import * as React from "react";
import { Input } from "@rebass/forms";
import { Box } from "rebass";

const SearchBox = ({ data, query, setQuery }) => {
  console.log("Props: ", data);
  // console.log("Value: ", value);
  return (
    <Box>
      <Input
        id="search"
        name="search"
        type="text"
        placeholder="Enter a search term"
        value={query}
        onChange={(event) => setQuery(event.target.value)}
      />
    </Box>
  );
};

export default SearchBox;