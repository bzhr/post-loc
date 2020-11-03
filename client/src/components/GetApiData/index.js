import * as React from "react";
import axios from "axios";

import { API_URL } from "../../constants";
import ContentBox from "../ContentBox";

const GetApiData = (props) => {
  const [query, setQuery] = React.useState("");
  const [data, setData] = React.useState([]);
  // const [isLoading, setIsLoading] = React.useState(true);
  // const url = query ? `${API_URL}?q=${query}` : API_URL;
  React.useEffect(() => {
    const lowerCaseQuery = query.toLowerCase();
    const fetchData = async () => {
      if (query.length >= 2) {
        console.log("Fetching data");
        const result = await axios(`${API_URL}?q=${lowerCaseQuery}`);
        setData(result.data);
      }
    };

    setTimeout(fetchData, 100);
  }, [query]);
  return (
    <ContentBox data={data} setQuery={setQuery} query={query}></ContentBox>
  );
};
export default GetApiData;
