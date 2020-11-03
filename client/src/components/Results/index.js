import * as React from "react";
import { Box, Flex, Text } from "rebass";

const Results = ({ data }) => {
  return (
    <Flex my={3} flexDirection="column">
      <Text fontSize={[3, 4, 5]} fontWeight="bold" color="primary">
        Results
      </Text>
      <Flex my={2} mx={6} flexDirection="column">
        {data.map((item) => (
          <Flex my={1} justifyContent="space-around" key={item.name}>
            <Box>{item.name}</Box>
            <Box>{item.postcode}</Box>
          </Flex>
        ))}
      </Flex>
    </Flex>
  );
};

export default Results;
