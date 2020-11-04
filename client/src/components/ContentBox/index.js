import * as React from "react";
import { Box, Flex } from "rebass";

import SearchBox from "../SearchBox";
import Suggestions from "../Suggestions";
import Results from "../Results";

const ContentBox = (props) => {
  return (
    <Box
      sx={{
        maxWidth: 600,
        mx: "auto",
        height: 250,
      }}
      bg="lightgray"
      width={[1, 1, 1 / 2]}
    >
      <Flex flexDirection="column">
        <SearchBox {...props} />
        <Suggestions {...props} />
        <Results {...props} />
      </Flex>
    </Box>
  );
};

export default ContentBox;
