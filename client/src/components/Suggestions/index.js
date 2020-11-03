import * as React from "react";
import { Box, Flex } from "rebass";

const Suggestions = ({ data, setQuery, query }) => {
  console.log(query);
  return (
    <Flex flexWrap="wrap" my={2}>
      {/* take the first 4 results for suggestions, not to break the ui */}
      {data.map((item) => (
        <Box my={1} mx={2} key={item.name} sx={{ cursor: "pointer" }}>
          {item.name.toLowerCase().includes(query) && (
            <Box onClick={() => setQuery(item.name)}>{item.name}</Box>
          )}
          {item.postcode.toLowerCase().includes(query) && (
            <Box onClick={() => setQuery(item.postcode)}>{item.postcode}</Box>
          )}
        </Box>
      ))}
    </Flex>
  );
};

export default Suggestions;
