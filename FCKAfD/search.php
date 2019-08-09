<?php
include("config.php");
include ("classes/SiteResultsProvider.php");

	if(isset($_GET["term"])) {
		$term = $_GET["term"];
	}
	else {
		exit("You must enter a search term");
	}

	$type = isset($_GET["type"]) ? $_GET["type"] : "sites";
	$page = isset($_GET["page"]) ? $_GET["page"] : 		1;	


	
?>
<!DOCTYPE html>
<html>
<head>
	<title>Liberté Egalité FCKAfDé</title>

	<link rel="stylesheet" type="text/css" href="assets/css/style.css">

</head>
<body>

	<div class="wrapper">
	
		<div class="header">


			<div class="headerContent">

				<div class="logoContainer">
					<a href="index.php">
						<img src="assets/images/icons/st,small,215x235-pad,210x230,f8f8f8.lite-1u1.jpg">
					</a>
				</div>

				<div class="searchContainer">

					<form action="search.php" method="GET">

						<div class="searchBarContainer">

							<input class="searchBox" type="text" name="term" value="<?php echo $term; ?>">
							<button class="searchButton">
								<img src="assets/images/icons/search.png">
							</button>
						</div>

					</form>

				</div>

			</div>


			<div class="tabsContainer">

				<ul class="tabList">

					<li class="<?php echo $type == 'Reden' ? 'active' : '' ?>">
						<a href='<?php echo "search.php?term=$term&type=sites"; ?>'>
							Reden
						</a>
					</li>

					<li class="<?php echo $type == 'tweets' ? 'active' : '' ?>">
						<a href='<?php echo "search.php?term=$term&type=images"; ?>'>
							Tweets
						</a>
					</li>

				</ul>


			</div>



		</div>

	<div class="mainResultSection">

		<?php 

			$resultsProvider = new SiteResultsProvider($con);
			$pageLimit = 20;

			$numResults = $resultsProvider->getNumResults($term);

			echo "<p class='resultsCount'>$numResults results found</p>";


			echo $resultsProvider->getResultsHtml(1,20, $term);

		?>
		

	</div>	

	</div>

</body>
</html>